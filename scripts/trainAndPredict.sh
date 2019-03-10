
echo "Initializing preprocessing"
python ../transformer/prepro.py

echo "Done"
echo "Initializing training"
python ../transformer/train.py

echo "Done"
echo "Entering evaluation mode. Talk to the chatbot via the prompt once the evaluation code is initialized."
echo "Initializing evaluation mode"
python ../transformer/eval.py
