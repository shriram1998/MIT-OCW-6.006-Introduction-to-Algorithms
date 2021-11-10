import string
import re
from nltk.corpus import stopwords
from collections import Counter
import math

para1 = "What is Lorem Ipsum? Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
para2 = "What is Lorem Ipsum? Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. Where does it come from?Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of 'de Finibus Bonorum et Malorum' (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, 'Lorem ipsum dolor sit amet..', comes from a line in section 1.10.32."
para2 = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)."
# para2 = para1
l1 = len(para1)
l2 = len(para2)
stopWords = stopwords.words("english")

pattern = re.compile(
    r'\b(' + r'|'.join(stopWords) + r')\b\s*')

translation_table = str.maketrans(string.punctuation+string.ascii_uppercase,
                                  " "*len(string.punctuation)+string.ascii_lowercase)
# lowercaseDoc = {i-32: i for i in range(97, 123)}


def punc(doc):
    return doc.translate(translation_table)


def stopWords(doc):
    return pattern.sub('', doc)


def count(doc):
    return Counter(doc.split())


def dotProduct(D1, D2):
    sum = 0.0
    if(l1 > l2):
        D1, D2 = D2, D1
    for key in D1:
        if key in D2:
            sum += (D1[key]*D2[key])
    return sum


para1 = count(stopWords(punc(para1)))
para2 = count(stopWords(punc(para2)))

dp = dotProduct(para1, para2)
mod1 = math.sqrt(sum(para1[k]*para1[k] for k in para1.keys()))
mod2 = math.sqrt(sum(para2[k]*para2[k] for k in para2.keys()))
similarity = (dp/(mod1*mod2))
print(similarity)
