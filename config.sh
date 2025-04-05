sudo apt update && sudo apt upgrade -y
sudo apt install unzip -y

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

sudo apt install python3-pip -y

sudo apt install python3-venv

python3 -m venv ambiente

source ambiente/bin/activate

pip install psutil
pip install numpy
pip install pandas
pip install boto3

python3 captura.py