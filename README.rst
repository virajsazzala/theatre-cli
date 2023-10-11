============================
theatre-cli
============================

Overview
--------

theatre-cli is a powerful command-line tool written in Python that transforms your terminal into a personal movie theater. With theatre-cli, you can effortlessly watch your favorite movies stored locally on your device. It provides a seamless and immersive movie-watching experience right from the command line.

Features
--------

- Watch movies conveniently using a text-based interface.
- Supports popular media players like mpv_ and VLC_.
- Easy-to-use setup and configuration.
- Compatible with Python 3.10 and higher.

Installation
------------

Prerequisites
^^^^^^^^^^^^^^^^^

Before you can enjoy theatre-cli, ensure you have the following dependencies installed:

- Python 3.10 (or higher)
- mpv_
- VLC_

Installation Steps
^^^^^^^^^^^^^^^^^^^

1. Clone the repository:

   .. code-block:: bash
   
      git clone https://github.com/virajsazzala/theatre-cli.git
      cd theatre-cli

2. Create a virtual environment:

   .. code-block:: bash

      python -m venv venv
      source venv/bin/activate

3. Install requirements:

   .. code-block:: bash

      pip install -r requirements.txt

4. Install the package in editable mode:

   .. code-block:: bash

      pip install -e .

Usage
-----

1. Launch theatre-cli by running the command provided above.
2. Follow the on-screen instructions to set up your movie directory.
3. Enjoy your movies with a cinematic experience right from your terminal.

Contributions
-------------

Contributions to theatre-cli are welcome! Whether you want to add features, fix bugs, or improve documentation, feel free to fork the repository and submit a pull request.

.. _mpv: https://mpv.io/
.. _VLC: https://www.videolan.org/vlc/
