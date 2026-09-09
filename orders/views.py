from django.shortcuts import render, get_object_or_404
from .models import Order, RefundRequest
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def orders_list(request):
    orders = Order.objects.filter(user=request.user)

    context = {
        "orders": orders,
    }

    print("orders==>", orders)
    return render(request, "order_templates/orders_list.html", context)


def order_details(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    refunds = RefundRequest.objects.filter(order=order)

    context = {"order": order, "refunds": refunds}
    return render(request, "order_templates/order_detail.html", context)
