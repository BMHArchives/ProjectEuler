#!/bin/sh
# To grant permissions to read, write and execute this script use: chmod 755 <script name>
echo "Creating new project folder."
cd ~/Development/GitHub/ProjectEuler
echo "Enter Project Name: "
read Project
echo "Creating folder $Project and adding README.md file."
mkdir -p $Project && touch $Project/README.md
echo "Folder and file created."
