from django.shortcuts import render
import data
from random import sample

tours_all = data.tours
departures = data.departures


# Create your views here.
def main_view(request):
    random_6_tours = dict(sample(tours_all.items(), 6))
    tours = {'tours': random_6_tours}
    return render(request, 'index.html', context=tours)


def departure_view(request, departure: str):
    tours_filter_by_city = {
        tour: tours_all[tour] for tour in tours_all
        if tours_all[tour]['departure'] == departure
    }

    additional_dict = {}
    additional_dict['from'] = departures[departure]
    additional_dict['count'] = len(tours_filter_by_city)
    additional_dict['night_min'] = min([tours_filter_by_city[tour]['nights'] for tour in tours_filter_by_city])
    additional_dict['night_max'] = max([tours_filter_by_city[tour]['nights'] for tour in tours_filter_by_city])
    additional_dict[departure] = 'active'
    tours = {'tours': tours_filter_by_city} | additional_dict
    return render(request, 'departure.html', context=tours)


def tour_view(request, id: int):
    departure = tours_all[id]['departure']
    departure_rus = departures[departure]
    return render(request, 'tour.html', context={**tours_all[id], 'from': departure_rus,
                                                 departure: 'active'})
