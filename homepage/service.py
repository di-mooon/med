from appointment.models import DateRecord, TimeRecord
import numpy as np


def create_cards_list(cards):
    dates = np.array(DateRecord.objects.all())
    cards_list = {}
    for card in cards:
        times = np.array(card.card_time.all()).reshape(-1, 11)
        time = {dates[x]: times[x] for x in range(5)}
        cards_list[card] = time
    return cards_list
