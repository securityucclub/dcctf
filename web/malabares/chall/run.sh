sudo docker build --rm -t "malabares" .
sudo docker run -d -p "0.0.0.0:7890:80" -h "malabares" --name="malabares" malabares
