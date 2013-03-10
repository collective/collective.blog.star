#!/bin/sh
PRODUCTNAME='collective.blog.star'
I18NDOMAIN=$PRODUCTNAME

# Synchronise the .pot with the templates.
i18ndude rebuild-pot --pot locales/${PRODUCTNAME}.pot --create ${I18NDOMAIN} ./configure.zcml

# Synchronise the resulting .pot with the .po files
i18ndude sync --pot locales/${PRODUCTNAME}.pot locales/*/LC_MESSAGES/${PRODUCTNAME}.po

WARNINGS=`find . -name "*pt" | xargs i18ndude find-untranslated | grep -e '^-WARN' | wc -l`
ERRORS=`find . -name "*pt" | xargs i18ndude find-untranslated | grep -e '^-ERROR' | wc -l`
FATAL=`find . -name "*pt"  | xargs i18ndude find-untranslated | grep -e '^-FATAL' | wc -l`

echo
echo "There are $WARNINGS warnings \(possibly missing i18n markup\)"
echo "There are $ERRORS errors \(almost definitely missing i18n markup\)"
echo "There are $FATAL fatal errors \(template could not be parsed, eg. if it\'s not html\)"
echo "For more details, run \'find . -name \"\*pt\" \| xargs i18ndude find-untranslated\' or"
echo "Look the rebuild i18n log generate for this script called \'rebuild_i18n.log\' on locales dir"

rm ./rebuild_i18n.log

touch ./rebuild_i18n.log

find ./ -name "*pt" | xargs i18ndude find-untranslated > rebuild_i18n.log
