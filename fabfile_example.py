#Se pordrá ejecutar comando de forma remota con la funcion RUN
#Ejecutar comandos como super usuario SUDO
from fabric.api import run, sudo, task, put, get, cd, prefix, local, env

#lista elementos dentro de un directorio
def show_dir():
    run('ls') 

#Crear nueva carpeta
def create_folder(folder):
    run('mkdir %s' %folder)

#Elimina carpeta
def delete_folder(folder):
    sudo ('rm -rf %s' %folder)

def pull():
    print('Obtenemos todos los cambios de la rama master!')

@task(alias='dp')
def deploy():
    pull()

#Suir archivo a servidor
@task
def upload_txt_file():
    put(
        #ruta de origen en local
        local_path='example.txt',
        #ruta destino en servidor remoto
        remote_path='./python-web'
    )

#Descargar archivo de servidor
@task
def get_txt_file(file):
    get(
        #Donde se va almacenar archivo a descargar
        local_path='./descargas',
        remote_path='./python-web/%s' %file
    )

#Movernos entre carpetas
@task
def pull():
    #Ejecuta en la raiz, cada funcion RUN se ejecuta uno a uno no secuencial
    #Para correr dos comando a la vez se puede:
    
    #CONCATENAR cCON &&
    #run('cd python-web && git pull')

    #USAR CONTEXTO cd que permite cambiar de directorio
    with cd('python-web'):
        run('git pull')

#Ejecutar comandos bajo contexto
@task
def install_requirements():
    #run('cd python-web && source env/bin/activate && pip install -r requirements.txt')
    with cd('python-web'):
        #FUNCION PARA EJECUTAR BAJO UN CONTEXTO
        with prefix('source env/bin/activate'):
            run('pip install -r requirements.txt')

#Ver elementos de equipo local
@task
def show_dir_local():
    local('ls -l')

#Indicar sobre que host y usuario se quiere ejecutar el comando
#Esto con el diccionario ENV
#Con comas puedo añadir mas host
env.hosts = ['104.248.228.195']

env.user = 'pamela'

#autenticarse con llave publica
env.key_filename = '~/.ssh/id_rsa.pub'

@task
def pull_env():
    with cd('python-web'):
        run('git-pull')