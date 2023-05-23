import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Actor, Genre


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    actors = [("George", "Klooney"),
              ("Kianu", "Reaves"),
              ("Scarlett", "Keegan"),
              ("Will", "Smith"),
              ("Jaden", "Smith"),
              ("Scarlett", "Johansson")]

    for genre in genres:
        Genre.objects.create(name=genre)

    for actor in actors:
        first_name, last_name = actor
        Actor.objects.create(first_name=first_name, last_name=last_name)

    # Update genre Dramma, set name to "Drama"
    Genre.objects.filter(name="Dramma").update(name="Drama")
    # Update actor George Klooney, set last_name to "Clooney"
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    # Update actor Kianu Reaves, set first_name to "Keanu"
    # and last_name to "Reeves"
    Actor.objects.filter(
        first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves"
    )

    # Delete genre Action
    Genre.objects.filter(name="Action").delete()
    # Delete all actresses with the first_name "Scarlett"
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")


if __name__ == "__main__":
    print(main())
