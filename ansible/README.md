# Налаштування робочої станції Ubuntu 26

Playbook встановлює базові системні та розробницькі утиліти з офіційних
репозиторіїв Ubuntu, а також pyenv для керування версіями Python. Він
розрахований на повторний запуск: вже встановлені пакети не перевстановлюються.
pyenv і його налаштування Bash встановлюються для користувача, від імені якого
запущено playbook.

## Запуск

Спочатку встановіть Ansible на Ubuntu:

```bash
sudo apt update
sudo apt install ansible
```

У корені цього репозиторію запустіть:

```bash
ansible-playbook -i localhost, --connection=local ansible/desktop.yml --ask-become-pass

ansible-playbook -i localhost, --connection=local ansible/desktop.yml -K -e "ansible_become_exe=sudo.ws"
```

Ansible попросить пароль користувача для виконання завдань із правами
адміністратора. Якщо користувач має налаштований `sudo` без пароля, прапорець
`--ask-become-pass` можна прибрати.

## Налаштування переліку програм

Змініть список `workstation_packages` у `desktop.yml`, щоб додати або прибрати
пакети. Playbook перевіряє, що цільова система — Ubuntu 26, оновлює кеш APT і
встановлює вказані пакети. Повне оновлення системи та сторонні репозиторії
навмисно не налаштовуються.

Після запуску відкрийте новий термінал або виконайте `source ~/.bashrc`.
Перевірити встановлення можна командою `pyenv --version`. Доступні версії Python
можна переглянути через `pyenv install --list`, а потім встановити потрібну та
вибрати її командою `pyenv install <версія>` і `pyenv global <версія>`.

## Lenovo ThinkStation P520 і лабораторні роботи

Playbook додатково готує станцію до лабораторних курсу:

- Docker (`docker.io`, `docker-compose-v2`) для lab4 і lab5; сервіс вмикається, а користувача додано до групи `docker` — **вийдіть із системи й увійдіть знову**, щоб група застосувалась. Перевірка: `docker run --rm hello-world`.
- Python 3.12 через pyenv (змінна `python_version`, встановлення з вихідного коду займає кілька хвилин) і `pipenv` через pipx — для lab2 і lab3. Перевірка: `python --version`, `pipenv --version`.
- `git-crypt`, `make`, `fwupd` (оновлення прошивок), `lm-sensors` і `smartmontools` (стан температур і дисків) для робочої станції.
- NVIDIA-драйвер (відеокарти Quadro/RTX у P520) вимкнений за замовчуванням. Увімкніть його так, потім перезавантажте ПК:

```bash
ansible-playbook -i localhost, --connection=local ansible/desktop.yml --ask-become-pass -e install_nvidia_driver=true
```
