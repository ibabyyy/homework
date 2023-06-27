def element_an_index(liste, index):
    try:
        element = liste[index]
        return element
    except IndexError:
        return None

# Beispielaufrufe
meine_liste = [1, 2, 3, 4, 5]
index_1 = 2
index_2 = 10

ergebnis_1 = element_an_index(meine_liste, index_1)
ergebnis_2 = element_an_index(meine_liste, index_2)

print("Ergebnis 1:", ergebnis_1)
print("Ergebnis 2:", ergebnis_2)

import boto3
import datetime

s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        bucketA_name = event['Records'][0]['s3']['bucket']['name']
        file_key = event['Records'][0]['s3']['object']['key']
        timestamp = datetime.datetime.now().strftime('%Y_%m_%d__%H_%M')

        message = f"A file named {file_key} was created in Bucket A at {timestamp}"

        # Create a new text file in Bucket B
        bucketB_name = 'bbbbb22222'
        new_file_name = f"{timestamp}.txt"
        s3.put_object(Bucket=bucketB_name, Key=new_file_name, Body=message)

        return {
            'statusCode': 200,
            'body': 'String generated and text file created in Bucket B successfully'
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': 'An error occurred'
        }


class ListTooShortError(Exception):
    pass

def element_an_index(liste, index):
    try:
        if len(liste) < 8:
            raise ListTooShortError("Die Liste ist zu kurz.")
        
        element = liste[index]
        return element
    except (IndexError, ListTooShortError) as e:
        print("Fehler:", str(e))
        return None

# Beispielaufrufe
meine_liste = [1, 2, 3, 4, 5]
index_1 = 2
index_2 = 10

ergebnis_1 = element_an_index(meine_liste, index_1)
ergebnis_2 = element_an_index(meine_liste, index_2)

print("Ergebnis 1:", ergebnis_1)
print("Ergebnis 2:", ergebnis_2)



import unittest

class TestIstSortiert(unittest.TestCase):
    def test_sortierte_liste(self):
        liste = [1, 2, 3, 4, 5]
        erwartet = True
        ergebnis = ist_sortiert(liste)
        self.assertEqual(ergebnis, erwartet)

    def test_unsortierte_liste(self):
        liste = [5, 3, 1, 4, 2]
        erwartet = False
        ergebnis = ist_sortiert(liste)
        self.assertEqual(ergebnis, erwartet)

if __name__ == '__main__':
    unittest.main()