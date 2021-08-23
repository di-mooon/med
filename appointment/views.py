from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.views.generic.base import View
from appointment.models import TimeRecord
from appointment.service import create_record
from .forms import PatientForm


class RecordTimeView(View):

    def post(self, request, *args, **kwargs):
        form = PatientForm(request.POST or None)
        if form.is_valid():
            time = TimeRecord.objects.filter(
                daterecord__id=kwargs.get('p'),
                card__id=kwargs.get('pk'),
                id=kwargs.get('k')
            )
            new_form = form.save(commit=False)
            new_form.name = form.cleaned_data['name']
            new_form.insurance = form.cleaned_data['insurance']
            new_form.phone = form.cleaned_data['phone']
            new_form.user = request.user
            form.save()

            time.update(patient_id=new_form.id, recorded=True, card_id=kwargs.get('pk'))

            messages.info(request, 'Вы успешно записались')
            return redirect("card_list")
        form = PatientForm()
        context = {'form': form,
                   }
        return render(request, 'record/record-create.html', context)

    def get(self, request, *args, **kwargs):
        form = PatientForm()
        time = TimeRecord.objects.get(
            daterecord__id=kwargs.get('p'),
            card__id=kwargs.get('pk'),
            id=kwargs.get('k')
        )
        if time.recorded:
            raise Http404
        context = {'form': form,
                   }

        return render(request, 'record/record-create.html', context)
