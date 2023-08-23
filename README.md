# Python with Qt on the console without an X11 Desktop

I run dedicated Python/Qt apps on several Pi 4 with the official 7" display.

I've seen several people ask how this is done so here's an example.

This is only tested on Rasperry Pi OS 11 / Bullseye

# Install the Code
Run the following commands as pi user in your home dir.

First install git and python3-venv, and a few pyside2 packages.

    sudo apt install python3-venv git
	sudo apt install python3-pyside2.qtcore python3-pyside2.qtgui python3-pyside2.qtnetwork python3-pyside2.qtqml python3-pyside2.qtquick python3-pyside2.qttest python3-pyside2.qtwidgets
	

Then create and activate a venv:

	python3 -m venv --system-site-packages ${HOME}/venv-gui
	
    . ${HOME}/venv-gui/bin/activate
    pip install --upgrade pip

Now clone the repo and install the application (-e means in editable mode)

	git clone https://github.com/lbt/python-gui
	cd python-gui
	pip install -e .
	
You can now run ./gui.py to run the clock.

Now we can create user systemd service so it runs on reboot.

Setup some variables in case you use a different user nowadays:

	USER="pi"
	GUI_PATH="${HOME}/python-gui"
	SYSTEMD_DIR=/home/${USER}/.config/systemd/user
	
Create the systemd directory and copy over the service file. (Note the pi user and path are hardcoded in the .service file so edit this if you need to change them).
	
	mkdir -p ${SYSTEMD_DIR}
	cp ${GUI_PATH}/gui.service $SYSTEMD_DIR/gui.service

Now tell systemd to read the config files we put in, enable it to run at reboot and then start the application.

	systemctl --user daemon-reload 
	systemctl --user enable gui
	systemctl --user start gui

Tell systemd's logind that this user would like a systemd session at reboot:

	sudo loginctl enable-linger ${USER}
