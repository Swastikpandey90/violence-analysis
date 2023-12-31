"""
A text tokenizer class , fully written from scratch.
"""


import re
import string
# Source: https://github.com/sanjaalcorps/NepaliStopWords/blob/master/NepaliStopWords.txt


STOP_WORDS = set("""अक्सर,अगाडि,अगाडी,अघि,अझै,अठार,अथवा,अनि,अनुसार,अन्तर्गत,अन्य,अन्यत्र,अन्यथा,अब,अरु,अरुलाई,अरू,अर्को,अर्थात,अर्थात्,अलग,अलि,अवस्था,अहिले,आए,आएका,आएको,आज,आजको,आठ,आत्म,आदि,आदिलाई,आफनो,आफू,आफूलाई,आफै,आफैँ,आफ्नै,आफ्नो,आयो,उ,उक्त,उदाहरण,उनको,उनलाई,उनले,उनि,उनी,उनीहरुको,उन्नाइस,उप,उसको,उसलाई,उसले,उहालाई,ऊ,एउटा,एउटै,एक,एकदम,एघार,ओठ,औ,औं,कता,कति,कतै,कम,कमसेकम,कसरि,कसरी,कसै,कसैको,कसैलाई,कसैले,कसैसँग,कस्तो,कहाँबाट,कहिलेकाहीं,का,काम,कारण,कि,किन,किनभने,कुन,कुनै,कुन्नी,कुरा,कृपया,के,केहि,केही,को,कोहि,कोहिपनि,कोही,कोहीपनि,क्रमशः,गए,गएको,गएर,गयौ,गरि,गरी,गरे,गरेका,गरेको,गरेर,गरौं,गर्छ,गर्छन्,गर्छु,गर्दा,गर्दै,गर्न,गर्नु,गर्नुपर्छ,गर्ने,गैर,घर,चार,चाले,चाहनुहुन्छ,चाहन्छु,चाहिं,चाहिए,चाहिंले,चाहीं,चाहेको,चाहेर,चोटी,चौथो,चौध,छ,छन,छन्,छु,छू,छैन,छैनन्,छौ,छौं,जता,जताततै,जना,जनाको,जनालाई,जनाले,जब,जबकि,जबकी,जसको,जसबाट,जसमा,जसरी,जसलाई,जसले,जस्ता,जस्तै,जस्तो,जस्तोसुकै,जहाँ,जान,जाने,जाहिर,जुन,जुनै,जे,जो,जोपनि,जोपनी,झैं,ठाउँमा,ठीक,ठूलो,त,तता,तत्काल,तथा,तथापि,तथापी,तदनुसार,तपाइ,तपाई,तपाईको,तब,तर,तर्फ,तल,तसरी,तापनि,तापनी,तिन,तिनि,तिनिहरुलाई,तिनी,तिनीहरु,तिनीहरुको,तिनीहरू,तिनीहरूको,तिनै,तिमी,तिर,तिरको,ती,तीन,तुरन्त,तुरुन्त,तुरुन्तै,तेश्रो,तेस्कारण,तेस्रो,तेह्र,तैपनि,तैपनी,त्यत्तिकै,त्यत्तिकैमा,त्यस,त्यसकारण,त्यसको,त्यसले,त्यसैले,त्यसो,त्यस्तै,त्यस्तो,त्यहाँ,त्यहिँ,त्यही,त्यहीँ,त्यहीं,त्यो,त्सपछि,त्सैले,थप,थरि,थरी,थाहा,थिए,थिएँ,थिएन,थियो,दर्ता,दश,दिए,दिएको,दिन,दिनुभएको,दिनुहुन्छ,दुइ,दुइवटा,दुई,देखि,देखिन्छ,देखियो,देखे,देखेको,देखेर,दोश्री,दोश्रो,दोस्रो,द्वारा,धन्न,धेरै,धौ,न,नगर्नु,नगर्नू,नजिकै,नत्र,नत्रभने,नभई,नभएको,नभनेर,नयाँ,नि,निकै,निम्ति,निम्न,निम्नानुसार,निर्दिष्ट,नै,नौ,पक्का,पक्कै,पछाडि,पछाडी,पछि,पछिल्लो,पछी,पटक,पनि,पन्ध्र,पर्छ,पर्थ्यो,पर्दैन,पर्ने,पर्नेमा,पर्याप्त,पहिले,पहिलो,पहिल्यै,पाँच,पांच,पाचौँ,पाँचौं,पिच्छे,पूर्व,पो,प्रति,प्रतेक,प्रत्यक,प्राय,प्लस,फरक,फेरि,फेरी,बढी,बताए,बने,बरु,बाट,बारे,बाहिर,बाहेक,बाह्र,बिच,बिचमा,बिरुद्ध,बिशेष,बिस,बीच,बीचमा,बीस,भए,भएँ,भएका,भएकालाई,भएको,भएन,भएर,भन,भने,भनेको,भनेर,भन्,भन्छन्,भन्छु,भन्दा,भन्दै,भन्नुभयो,भन्ने,भन्या,भयेन,भयो,भर,भरि,भरी,भा,भित्र,भित्री,भीत्र,म,मध्य,मध्ये,मलाई,मा,मात्र,मात्रै,माथि,माथी,मुख्य,मुनि,मुन्तिर,मेरो,मैले,यति,यथोचित,यदि,यद्ध्यपि,यद्यपि,यस,यसका,यसको,यसपछि,यसबाहेक,यसमा,यसरी,यसले,यसो,यस्तै,यस्तो,यहाँ,यहाँसम्म,यही,या,यी,यो,र,रही,रहेका,रहेको,रहेछ,राखे,राख्छ,राम्रो,रुपमा,रूप,रे,लगभग,लगायत,लाई,लाख,लागि,लागेको,ले,वटा,वरीपरी,वा,वाट,वापत,वास्तवमा,शायद,सक्छ,सक्ने,सँग,संग,सँगको,सँगसँगै,सँगै,संगै,सङ्ग,सङ्गको,सट्टा,सत्र,सधै,सबै,सबैको,सबैलाई,समय,समेत,सम्भव,सम्म,सय,सरह,सहित,सहितै,सही,साँच्चै,सात,साथ,साथै,सायद,सारा,सुनेको,सुनेर,सुरु,सुरुको,सुरुमै,सो,सोचेको,सोचेर,सोही,सोह्र,स्थित,स्पष्ट,हजार,हरे,हरेक,हामी,हामीले,हाम्रा,हाम्रो,हुँदैन,हुन,हुनत,हुनु,हुने,हुनेछ,हुन्,हुन्छ,हुन्थ्यो,हैन,हो,होइन,होकि,होला,नेपाल,जिल्ला,प्रदेशअनुसार,प्रदेश,गरेरै,अंशत,मूलत,सर्वत,प्रथमत,सम्भवत,सामान्यत,विशेषत,प्रत्यक्षत,मुख्यत,स्वरुपत,अन्तत,पूर्णत,फलत,क्रमश,अक्षरश,प्रायश,कोटिश,शतश,शब्दश,आ-आफ्नो,आ-आफ्ना, उन, लगिए, लगाए, झनै, गराए, लगे, बस्न, गत, थिइन्, बताइन्, गरिए, ल्याए, राखेर, सहित, तीन, आइतबार, काठमाडौं–,""".split(','))

DISTRICT_NAME = set("""कोशी,भोजपुर,धनकुटा,इलाम,झापा,खोटाङ,मोरङ,ओखलढुङ्गा,पाँचथर,संखुवासभा,सोलुखुम्बु,सुनसरी,ताप्लेजुङ,तेह्रथुम,उदयपुर,मधेस,बारा,पर्सा,धनुषा,महोत्तरी,रौतहट,सप्तरी,सर्लाही,सिराहा,बागमती,भक्तपुर,चितवन,धादिङ,दोलखा,काठमाण्डौं,काभ्रेपलाञ्चोक,ललितपुर,मकवानपुर,नुवाकोट,रामेछाप,रसुवा,सिन्धुली,सिन्धुपाल्चोक,गण्डकी,बागलुङ,गोरखा,कास्की,लमजुङ,मनाङ,मुस्ताङ,म्याग्दी,नवलपरासी,पर्वत,स्याङ्जा,तनहुँ,लुम्बिनी,अर्घाखाँची,बाँके,बर्दिया,दाङ,पूर्वी रुकुम,गुल्मी,कपिलवस्तु,परासी,पाल्पा,प्युठान,रोल्पा,रुपन्देही,कर्णाली,दैलेख,डोल्पा,हुम्ला,जाजरकोट,जुम्ला,कालिकोट,मुगु,सल्यान,सुर्खेत,पश्चिमी रुकुम,सुदुरपश्चिम,अछाम,बैतडी,बझाङ,बाजुरा,डडेल्धुरा,दार्चुला,काठमाडौँ,नगरपालिका""".split(','))

SUFFIX = ["का","मा","भर","कै","की","को","मै","ले","तिर","वोध","झैं","बिच","जति","वटा","योस","अघि","बोध","बीच","भरी","संग","पटक","पनि","माझ","भरि","सँग","विच","वाट","पछि","लाइ","भयो","लाई","साथ","बीच","शील","तीर","बाट","हरू","हरु","सित","वीच","पछी","मुनि","बासि","मुनी","ज्यु","ज्यू","पाली","सङ्ग","वासी","मुलक","जीले","मूलक","निकट","पारि","पारी","वारि","जीकै","मुखी","जीको","सम्म","वासि","योस्","बारे","माथी","माझै","कहां","सामु","संगै","तर्फ","सँगै","सङ्ग","मध्य","चाहि","भएकी","वारे","बाटै","समेत","माथि","बिना","कहाँ","देखि","सहित","बासी","साथै","काहां","मात्र","पर्यो","वर्षे","भित्र","प्रती","सहितै","लगायत","भन्दा","खालको","लगाएत","बाहेक","हरूको","जस्तै","लार्इ","भित्र","हरुकै","हरूमै","कर्ता","पूर्व","हरूका","बीचमा","बिचमा","बिहीन","बिचको","बिहिन","बीचको","हरुले","हरूले","हरुमा","हरूमा","हरुमै","हरुको","जस्ता","हरुका","जस्तो","जीहरू","जिहरु","रुपमा","जीहरु","काहाँ","हरूकै","पुर्ब","मध्ये","पूर्ब","प्रति","पुर्ण","रुपले","रूपले","सँगको","पुर्व","रूपमा","पूर्ण","पछिका","विहिन","पछीको","पछिको","अगाडि","पट्टि","सकेका","विहीन","स्थित","पर्ने","समक्ष","समेतै","सम्मै","सङ्गै","संगको","सकेको","जिहरू","बमोजिम","हरूसँग","हरुसँग","सहितका","हरूसंग","हरूझैं","माथीको","हरुबाट","सम्ममा","हरूबीच","भित्रै","कोलागी","हरूबाट","माथिको","हरूवाट","हरुझैं","पस्चात","मध्यका","तिरबाट","वारेमा","तर्फको","बारेमा","देखीको","द्वारा","द्धारा","हरूसित","हरुवाट","सम्मले","विनाका","ज्यूले","पल्टको","सम्मको","हरुबीच","बिहीनै","बिहिनै","बिनाका","मार्फत","सहीतका","देखिको","मात्रै","राखेको","हरुसंग","पश्चात","तर्फका","पद्धति","हरुसित","अनुसार","हरुलाइ","हरूलाई","हरुलाई","हरूलाइ","ज्युले","पुर्बक","पूर्वक","पुर्वक","ज्युकै","ज्युको","पूर्बक","लगायतका","हरूसितै","लगायतले","पूर्वकै","लगायतको","पुर्वकै","पुर्बकै","भित्रको","पूर्बकै","बिरुद्द","बिरूद्द","ज्यूहरु","लगायतमा","लगाएतले","हरुसितै","ज्यूहरू","ज्युहरु","लगाएतका","लगाएतमा","विरुद्द","विरूद्द","लगाएतको","मार्फतै","विरुद्ध","ज्युहरू","हरुमाथी","भीत्रको","भित्रमा","पट्टिको","पश्चात्","हरूसंगै","हरुमाथि","हरूसम्म","हरुसङ्ग","हरूसङ्ग","हरूमाथी","मध्येका","हरुसम्म","हरुसमेत","हरूसमेत","हरुसंगै","हरूमध्य","हरुमध्य","हरुसँगै","हरूसँगै","मुन्तिर","भित्रकै","हरूमाथि","भित्रका","रहेकाहरु","हरूसमक्ष","हरुसमक्ष","रहेकाहरू","हरुसंगको","हरूसंगको","हरुमध्ये","हरूसम्मै","हरुसँगको","हरूप्रति","लगायतसँग","हरूसँगको","सम्बन्धी","सम्बन्धि","हरुप्रती","हरुसम्मै","हरूमध्ये","पट्टितिर","बित्तिकै","हरूप्रती","हरुप्रति","हरुसम्ममा","हरूद्धारा","विरुद्दको","हरुद्धारा","हरुसङ्गको","बिरूद्दको","बिरुद्दको","भित्रसमेत","हरूसङ्गको","विरूद्दको","हरूसम्ममा","रहेको","रहेका","रहेकी","लगत्तै"]

# stop_words = list(map(lambda s: s.strip(), stop_words))
stop_words = STOP_WORDS



class NepaliTokenizer:
    
    def __init__(self ,punct=[]):
        """
        #Parameter:

        punct-> Punctuation (Input your own punctuation)

        """

        self.user_defined_punctuation = punct
        self.punctuation = ["\ufeff" , '\n' , '<br>' , '॥','।', ',', '-', '—', '–'] + list(string.punctuation)

        if self.user_defined_punctuation:
            self.punctuation += self.user_defined_punctuation
    
    def remove_special_characters(self, text):
        """this method is used to remove special characters

        Args:
            text (string): string from where characters needs to be removed

        Returns:
            string: string with no any given special character
        """
        string = re.sub('[।(),०-९<<?!,—,–,/,’,‘,:,\u200d]', ' ', text)
        return string
    
    def tokenizer(self , text):
        """
        Input text corpus to tokenize.

        #Parameter:
        
        ---- text(str)-> returns list.

        """


        for punct in self.punctuation:
            text = ' '.join(text.split(punct))

        text = re.sub('\d+' , ' ',text)

        text = text.split(' ')
        nepali_tokens = []

        for t in text:
            if t not in stop_words and t not in DISTRICT_NAME and t not in SUFFIX:
                if t != '' and t not in self.punctuation:
                    nepali_tokens.append(t)

        return nepali_tokens

    
    def __str__(self):
        return 'Input extra punctuation for tokenizing a corpus.'
        
