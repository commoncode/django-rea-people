from . import factories

def make_objects():

    company1 = factories.OrganisationFactory()

    company2 = factories.OrganisationFactory(
        name="Montage Software",
        number="0414907075",
        interest_in_courses=False
    )

    company3 = factories.OrganisationFactory(
        name="Two Bulls",
        number="0432902707",
        interest_in_courses=True
    )


    person1 = factories.PersonFactory(
        name="David Micallef",
        email="dave@montagesoftware.com.au",
        position="Sole Trader",
        organisation= company2
    )

    person2 = factories.PersonFactory(
        name="Tim Mutton",
        email="tim.mutton@two-bulls.com",
        organisation= company3
    )

    EpitomeInstance1 = factories.EpitomeInstanceFactory(
        person=person1,
    )

    EpitomeInstance2 = factories.EpitomeInstanceFactory(
        person=person2,
    )

    RatingInstance1 = factories.RatingInstanceFactory(
        epitome_instance=EpitomeInstance1,
        value=3
    )

    RatingInstance2 = factories.RatingInstanceFactory(
        epitome_instance=EpitomeInstance2,
        value=1
    )






