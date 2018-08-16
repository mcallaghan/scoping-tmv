from django.core.management import utils
import getpass

sc = utils.get_random_secret_key().replace('$','x')
db_username = input("Enter database username: ")
db_password = getpass.getpass("Enter database password: ")
db_name = input("Enter database name: ")
settings_path=input("What settings path would you like to use ? Options are local or production")
#print(db_url)
settings_path = 'config.settings.{}'.format(settings_path)
with open('.env','w') as f:
    f.write('DEBUG=OFF\n')
    f.write('SECRET_KEY={}\n'.format(sc))
    f.write('DB_NAME={}\n'.format(db_name))
    f.write('DB_USER={}\n'.format(db_username))
    f.write('DB_PASSWORD={}\n'.format(db_password))
    f.write('DJANGO_SETTINGS_PATH={}\n'.format(settings_path))
