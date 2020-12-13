import json
import sys
from googletrans import Translator
import time, os

file = open('/home/maulik/Downloads/intl_messages.arb')
fileString = file.read()

path = file.name[:file.name.rindex('/')+1]
print(path)
parsedJson = json.loads(fileString)
translator = Translator()

for item in parsedJson:
    if not item[0] == '@':
        translatedString = translator.translate(parsedJson[item], src='en', dest='gu').text
        time.sleep(0.5)
        parsedJson[item] = translatedString
        print(parsedJson[item])

# print('=========Translated JSON =========\n')
# print(json.dumps(parsedJson, ensure_ascii=False, indent=4))

newFile = open(path+'intl_'+languageCode+'.arb', 'w')
newFile.write(json.dumps(parsedJson, indent=4))

command = "flutter pub run intl_translation:generate_from_arb --output-dir=lib/l10n " \
          "--no-use-deferred-loading lib/l10n/intl_messages.arb lib/l10n/intl_"+languageCode+".arb " \
          "lib/Utils/GenericLocalizations.dart"
os.system(command)
