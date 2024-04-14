import paramiko
import psycopg2
# Установка соединения с хостом
def connect_to_host(host, username, password):    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())    ssh.connect(host, username=username, password=password)
    return ssh
# Установка ПО на хостеdef install_software_on_host(ssh, software_name):
    command = f"sudo apt-get install {software_name} -y"  # Пример команды для установки ПО    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.read().decode('utf-8')    print(output)
# Интерактивное взаимодействие с PostgreSQL
def interact_with_postgresql(dbname, user, password, host):    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    cursor = conn.cursor()
    cursor.execute("SELECT version();")    record = cursor.fetchone()
    print("Вы подключились к базе данных PostgreSQL")    print("Версия сервера:", record)

    cursor.close()    conn.close()
# Запуск скрипта на сервере ALTLinux
def run_script_on_altlinux_server(ssh, script_name):    command = f"bash {script_name}"
    stdin, stdout, stderr = ssh.exec_command(command)    output = stdout.read().decode('utf-8')
    print(output)
# Главная функцияdef main():
    host = 'ip_адрес_хоста'    username = 'ваше_имя_пользователя'
    password = 'ваш_пароль'    software_name = 'название_программы'
    altlinux_script = 'altlinux_server_script.sh'  # Скрипт на сервере ALTLinux    dbname = 'название_базы_данных'
    user = 'пользователь'    db_password = 'пароль_от_базы'
    db_host = 'хост_базы_данных'
    ssh = connect_to_host(host, username, password)    install_software_on_host(ssh, software_name)
    run_script_on_altlinux_server(ssh, altlinux_script)    interact_with_postgresql(dbname, user, db_password, db_host)
    ssh.close()
if name == "__main__":
    main()