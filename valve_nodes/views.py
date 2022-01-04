from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse, Http404
from django.views.generic import View
from .models import ValveNode, MeterDevice
from .forms import ValveNodeForm


def main(request):
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render(request, 'valve_nodes/index.html', {'dt': dt})
    # return HttpResponse('Hello! You in main page! Coming soon!')


""" ======================= Общие классы для обработки однотипных запросов по показу и вводу форм ======================
"""


class ObjectViewMixin:
    """
    Класс для объединения повторений запросов  ====показа СПИСКОВ==== (КУ, СИ, телемеханика и т.д.)
    """
    model = None
    template = None

    def get(self, request):
        obj_list = self.model.objects.all()
        return render(request, self.template, {'form': obj_list})


class ObjectDetailMixin:
    """
    Класс для объединения повторений запросов для ====показа ОБЪЕКТОВ==== из списка (КУ, СИ, телемеханика и т.д.)
    """
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})


class ObjectAddMixin:
    """
    Класс для объединения повторений запросов для =====ДОБАВЛЕНИЯ экземпляров===== (КУ, СИ, телемеханика и т.д.)
    """
    model_form = None
    template = None

    def get(self, request):
        form = self.model_form()
        return render(request, self.template, context={'form': form})

    def post(self, request, *args, **kwargs):
        bound_form = self.model_form(request.POST)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})


class ObjectUpdateMixin:
    model = None
    model_form = None
    template = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(instance=obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(request.POST, instance=obj)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})


class ObjectDeleteMixin:
    model = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.redirect_url))


"""============================== Целевые Вьюшки по типам Обьектов ==================================
"""


class ValvesView(ObjectViewMixin, View):
    """
    Дочерний класс для показа СПИСКА крановых узлов
    """
    model = ValveNode
    template = 'valve_nodes/index.html'


class ValveDetail(ObjectDetailMixin, View):
    """
    Дочерний класс для показа крановых узлов
    """
    model = ValveNode
    template = 'valve_nodes/valve_detail.html'


class ValveAdd(ObjectAddMixin, View):
    model_form = ValveNodeForm
    template = 'valve_nodes/add_valve.html'


class ValveUpdate(ObjectUpdateMixin, View):
    model = ValveNode
    model_form = ValveNodeForm
    template = 'valve_nodes/valve_update.html'


class ValveDelete(ObjectDeleteMixin, View):
    model = ValveNode
    template = 'valve_nodes/valve_delete.html'
    redirect_url = 'valves_node_list'
