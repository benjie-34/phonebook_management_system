from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ContactForm
from .models import Contact

def contact_list(request):
    query = request.GET.get("q", "").strip()
    contacts = Contact.objects.all()
    if query:
        contacts = contacts.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(phone_number__icontains=query) |
            Q(email__icontains=query)
        )
    paginator = Paginator(contacts, 10)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(request, "contacts/contact_list.html", {
        "page_obj": page_obj,
        "query": query,
        "total_contacts": Contact.objects.count(),
    })

def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, "contacts/contact_detail.html", {"contact": contact})

def contact_create(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            messages.success(request, f"{contact.full_name} was added to your phone book.")
            return redirect("contact_detail", pk=contact.pk)
    else:
        form = ContactForm()
    return render(request, "contacts/contact_form.html", {"form": form, "page_title": "Add Contact"})

def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, f"{contact.full_name}'s details were updated.")
            return redirect("contact_detail", pk=contact.pk)
    else:
        form = ContactForm(instance=contact)
    return render(request, "contacts/contact_form.html", {
        "form": form, "page_title": "Edit Contact", "contact": contact
    })

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        name = contact.full_name
        contact.delete()
        messages.success(request, f"{name} was deleted.")
        return redirect("contact_list")
    return render(request, "contacts/contact_confirm_delete.html", {"contact": contact})
