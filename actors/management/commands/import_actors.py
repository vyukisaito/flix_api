import csv  # biblioteca nativa do python
from datetime import datetime
from django.core.management.base import BaseCommand
from actors.models import Actor  # importa Actor para poder fazer o cadastro


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do arquivo com atores',
        )

    def handle(self, *args, **options):
        file_name = options['file_name']

        with open(file_name, 'r', encoding='utf-8') as file:  # abrindo o arquivo
            reader = csv.DictReader(file)  # ler o arquivo
            for row in reader:  # percorre linha a linha
                name = row['name']
                birthday = datetime.strptime(row['birthday'], '%Y-%m-%d').date()  # le certo o arquivo quem tem data
                nationality = row['nationality']

                self.stdout.write(self.style.NOTICE(name))

                Actor.objects.create(
                    name=name,
                    birthday=birthday,
                    nationality=nationality,
                )

        self.stdout.write(self.style.SUCCESS('ATORES IMPORTADOS COM SUCESSO!'))  # print tunado do djano command
