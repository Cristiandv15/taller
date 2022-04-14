import email
from unicodedata import name
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render
from proyectofinal.taller.models import Propietario, Taller, Vehiculo
from .forms import PropietarioForms, VehiculoForms, TallerForms


 
class PropietarioView(TemplateView):
    template_name = 'crud/propietario.html'

    def get(self, request):
        context = {
            'propietarios': Propietario.objects.all()
        }
        return render(request,self.template_name, context)

class PropietarioDeleteView(TemplateView):
    template_name = 'crud/propietario.html'

    def get(self, request, propietario_id):

        propietario = Propietario.objects.get(id=propietario_id)
        propietario.delete()

        
        context = {
            'propietarios': Propietario.objects.all()
        }

        return render(request,self.template_name, context)


class PropietarioCreateUpdateView(TemplateView):
    template_name = 'crud/crear-propietario.html'

    def get(self, request, propietario_id=None):
        propietario = None
        if propietario_id:
            propietario = Propietario.objects.get(id=propietario_id)

        if propietario:
            # Update
            context = {
                'form': PropietarioForms(
                    initial={
                        'name': propietario.name,
                        'lastname': propietario.lastname,
                        'email': propietario.email,
                        
                    }
                )
            }
        else:
            # Create
            context = {
                'form': PropietarioForms()
            }

        return render(request,self.template_name, context)

    def post(self, request, propietario_id=None):
        obj_post = request.POST

        # Forma avanzada
        Propietario.objects.update_or_create(
            email=obj_post.get('email'), # -> filter
            defaults={
                'name': obj_post.get('name'),
                'lastname': obj_post.get('lastname'),
            }
        )

        context = {
            'form': PropietarioForms()
        }

        return render(request,self.template_name, context)


class VehiculoView(TemplateView):
    template_name = 'crud/vehiculo.html'

    def get(self, request):
        context = {
            'vehiculos': Vehiculo.objects.all()
        }
        return render(request,self.template_name, context)

class VehiculoDeleteView(TemplateView):
    template_name = 'crud/vehiculo.html'

    def get(self, request, vehiculo_id):

        vehiculo = Vehiculo.objects.get(id=vehiculo_id)
        vehiculo.delete()

        
        context = {
            'vehiculos': Vehiculo.objects.all()
        }

        return render(request,self.template_name, context)


class VehiculoCreateUpdateView(TemplateView):
    template_name = 'crud/crear-vehiculo.html'

    def get(self, request, vehiculo_id=None):
        vehiculo = None
        if vehiculo_id:
            vehiculo = Vehiculo.objects.get(id=vehiculo_id)

        if vehiculo:
            # Update
            context = {
                'form': VehiculoForms(
                    initial={
                        'mark': vehiculo.mark,
                        'model': vehiculo.model,
                        'patent': vehiculo.patent,
                        
                    }
                )
            }
        else:
            # Create
            context = {
                'form': VehiculoForms()
            }

        return render(request,self.template_name, context)

    def post(self, request, vehiculo_id=None):
        obj_post = request.POST

        # Forma avanzada
        Vehiculo.objects.update_or_create(
            patent=obj_post.get('patent'), # -> filter
            defaults={
                'mark': obj_post.get('mark'),
                'model': obj_post.get('model'),
            }
        )

        context = {
            'form': VehiculoForms()
        }

        return render(request,self.template_name, context)

class TallerView(TemplateView):
    template_name = 'crud/taller.html'

    def get(self, request):
        context = {
            'talleres': Taller.objects.all()
        }
        return render(request,self.template_name, context)

class TallerDeleteView(TemplateView):
    template_name = 'crud/taller.html'

    def get(self, request, taller_id):

        taller = Taller.objects.get(id=taller_id)
        taller.delete()

        
        context = {
            'talleres': Taller.objects.all()
        }

        return render(request,self.template_name, context)


class TallerCreateUpdateView(TemplateView):
    template_name = 'crud/crear-taller.html'

    def get(self, request, taller_id=None):
        taller = None
        if taller_id:
            taller = Taller.objects.get(id=taller_id)

        if taller:
            # Update
            context = {
                'form': TallerForms(
                    initial={
                        'name': taller.name,
                        'address': taller.address,
                        'city': taller.city,
                        
                    }
                )
            }
        else:
            # Create
            context = {
                'form': TallerForms()
            }

        return render(request,self.template_name, context)

    def post(self, request, taller_id=None):
        obj_post = request.POST

        # Forma avanzada
        Taller.objects.update_or_create(
            address=obj_post.get('address'), # -> filter
            defaults={
                'name': obj_post.get('name'),
                'city': obj_post.get('city'),
            }
        )

        context = {
            'form': TallerForms()
        }

        return render(request,self.template_name, context)

    
class SearchView(TemplateView):
    template_name = 'forms/search.html'

    def post(self, request):
        
        #print('taller')
        print(request.POST.get('email'))
        context = {
            "elements": Propietario.objects.filter(
                email__icontains=request.POST.get('email')
            )
        }


        return render(request, self.template_name, context)
