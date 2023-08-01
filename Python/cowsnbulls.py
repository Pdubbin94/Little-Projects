{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import random"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def getDigits(num):\n",
    "    return [int(i) for i in str(num)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def noDuplicates(num):\n",
    "    num_li = getDigits(num)\n",
    "    if len(num_li) == len(set(num_li)):\n",
    "        return True\n",
    "    else: \n",
    "        return False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "def generateNum():\n",
    "    while True:\n",
    "        num = random.randint(1000,9999)\n",
    "        if noDuplicates(num):\n",
    "            return num"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def numOfBullsCows(num,guess):\n",
    "    bull_cow = [0,0]\n",
    "    num_li = getDigits(num)\n",
    "    guess_li =getDigits(guess)\n",
    "\n",
    "    for i,j in zip(num_li,guess_li):\n",
    "        if j in num_li :\n",
    "            if j == i:\n",
    "                bull_cow[0] += 1\n",
    "            else:\n",
    "                bull_cow[1] += 1\n",
    "    return bull_cow\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter 4 digit nummber only. Try again.\n",
      "1 bulls, 1 cows\n",
      "0 bulls, 2 cows\n",
      "1 bulls, 0 cows\n",
      "You ran out of tries. Number was 5217\n"
     ]
    }
   ],
   "source": [
    "num = generateNum()\n",
    "tries = int(input('Enter number of tries: '))\n",
    "\n",
    "while tries > 0:\n",
    "    guess = int(input(\"Enter your guess: \"))\n",
    "    if not noDuplicates(guess):\n",
    "        print(\"Number should not have repeated digits. Try again.\")\n",
    "        continue\n",
    "    if guess < 1000 or guess > 9999:\n",
    "        print(\"Enter 4 digit nummber only. Try again.\")\n",
    "        continue\n",
    "    bull_cow = numOfBullsCows(num, guess)\n",
    "    print(f\"{bull_cow[0]} bulls, {bull_cow[1]} cows\")\n",
    "    tries -=1\n",
    "\n",
    "    if bull_cow[0] == 4:\n",
    "        print(\"You guessed right!\")\n",
    "        break\n",
    "else:\n",
    "    print(f\"You ran out of tries. Number was {num}\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
