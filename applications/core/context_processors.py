from .form import ContactForm, NewsletterForm


def site_context_manager(request):
    return dict(
        site_address="4517 Washington Ave. Manchester, Kentucky 39495",
        office_hours="8:00 - 17:00, Mon - Sat",
        opperation_hours="24/7, Mon - Mon",
        site_contact="254745547755",
        contact_form=ContactForm(),
        newsletter_form=NewsletterForm(),
    )
