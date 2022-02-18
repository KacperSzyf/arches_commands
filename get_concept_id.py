from django.core.management.base import BaseCommand, CommandError
from arches.app.models.models import Concept as modelConcept
from arches.app.models.concept import Concept


class Command(BaseCommand):
    """
    Commands for returning preflabel and uuid of concepts in a thesauri
    """

    def handle(self, *args, **options):

        source_thesauri_id = "117cddf0-8403-4e16-b325-43327efc9e1f"
        target_thesauri_id = "06cf74db-f2b8-46a9-8c2f-565bedaa6424"

        for conceptid in [source_thesauri_id, target_thesauri_id]:
            c = Concept().get(
                id=conceptid,
                include_subconcepts=True,
                include_parentconcepts=False,
                include_relatedconcepts=True,
                depth_limit=None,
                up_depth_limit=None,
            )
            print({c.values[0].value: conceptid})
            for subc in c.subconcepts:
                print(vars(subc.values[0]))
                print({subc.values[0].value: subc.values[0].id})
            print("------------------------------------")