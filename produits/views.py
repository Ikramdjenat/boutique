from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from decimal import Decimal


# عرض قائمة المنتجات
def liste_produits(request):
    produits = Product.objects.all()
    return render(request, 'produits/liste_produits.html', {'produits': produits})

# عرض تفاصيل منتج معين
def detail_produit(request, produit_id):
    produit = get_object_or_404(Product, id=produit_id)
    return render(request, 'produits/detail_produit.html', {'produit': produit})

# إضافة منتج إلى السلة
def ajouter_au_panier(request, produit_id):
    produit = get_object_or_404(Product, id=produit_id)

    # نحصل على السلة من السيشن أو ننشئ واحدة جديدة
    panier = request.session.get('panier', {})

    # إذا كان المنتج موجود في السلة، نزيد الكمية
    if str(produit_id) in panier:
        panier[str(produit_id)] += 1
    else:
        panier[str(produit_id)] = 1

    # نحدث السلة في السيشن
    request.session['panier'] = panier

    # نعيد التوجيه إلى صفحة تفاصيل المنتج
    return redirect('detail_produit', produit_id=produit_id)

def afficher_panier(request):
    panier = request.session.get('panier', {})
    produits = []
    total = 0

    for produit_id, quantite in panier.items():
        produit = get_object_or_404(Product, id=int(produit_id))
        total_produit = produit.prix * quantite  # ✅ احسب المجموع لكل منتج
        produits.append({
            'produit': produit,
            'quantite': quantite,
            'total': total_produit
        })
        total += total_produit  # ✅ اجمع السعر الكلي لكل منتج

    return render(request, 'produits/panier.html', {
        'produits': produits,
        'total': total
    })
def supprimer_du_panier(request, produit_id):
    panier = request.session.get('panier', {})
    produit_id_str = str(produit_id)

    if produit_id_str in panier:
        del panier[produit_id_str]  # نحذف المنتج من القاموس

    request.session['panier'] = panier
    return redirect('afficher_panier')
def afficher_panier(request):
    from decimal import Decimal

    panier = request.session.get('panier', {})
    produits = []
    sous_total = Decimal('0.00')

    for produit_id, quantite in panier.items():
        produit = get_object_or_404(Product, id=int(produit_id))
        total_produit = produit.prix * quantite
        produits.append({
            'produit': produit,
            'quantite': quantite,
            'total': total_produit
        })
        sous_total += total_produit

    frais_livraison = Decimal('5.00')
    remise = Decimal('0.10')
    montant_remise = sous_total * remise
    total_general = sous_total + frais_livraison - montant_remise

    return render(request, 'produits/panier.html', {
        'produits': produits,
        'sous_total': sous_total,
        'frais_livraison': frais_livraison,
        'montant_remise': montant_remise,
        'total': total_general
    })

