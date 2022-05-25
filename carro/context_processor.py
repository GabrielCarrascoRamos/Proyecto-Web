def importe_total_carro(request):
    
    if request.user.is_authenticated:
        total = 0
        for key, value in request.session["carro"].items():
            total=total+float(value["precio"])*value["cantidad"]
    
    return {"importe_total_carro":total}