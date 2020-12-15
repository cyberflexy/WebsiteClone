import requests
import os
from bs4 import BeautifulSoup
import re
from fake_useragent import UserAgent

# pip install fake-useragent
# pip install beautifulsoup4
# pip install requests


class cloner:
    def __init__(self, url, folder):
        self.url = url
        self.folder = folder
        # self.header = {'User-Agent': header}

     # METHOD TO REPLACE ALL INTERNAL FILES/PAGES FORMAT AS .html
    def smooth_replace(self, place):
        place = place.replace(".php", ".html").replace(".aspx", ".html").replace(
            ".asp", ".html").replace(".py", ".html").replace(".jsp", ".html")
        return place

     # METHOD TO REMOVE BYTES ADDED TEXTS
    def byte_replace(self, content):
        recov = content
        recov = recov.replace("\\n", "")
        recov = recov.replace("b'", "")
        recov = recov.replace("\\t", "")
        recov = recov.replace("\\xc2", "")
        recov = recov.replace("\\xa9", "")
        recov = recov.replace("\\x00", "")
        recov = recov.replace("\\r", "")
        recov = recov.replace("\\s", "")
        recov = recov.replace("\\xd1", "")
        recov = recov.replace("\\x80", "")
        recov = recov.replace("\\xd0", "")
        recov = recov.replace("\\x83", "")
        recov = recov.replace("\\x81", "")
        recov = recov.replace("\\xba", "")
        recov = recov.replace("\\xb8", "")
        recov = recov.replace("\\xb9", "")
        recov = recov.replace("\\xd9", "")
        recov = recov.replace("\\xd8", "")
        recov = recov.replace("\\xa7", "")
        recov = recov.replace("\\xb1", "")
        recov = recov.replace("\\xb3", "")
        recov = recov.replace("\\xdb", "")
        recov = recov.replace("\\x8c", "")
        recov = recov.replace("\\xe0", "")
        recov = recov.replace("\\xa4", "")
        recov = recov.replace("\\xbf", "")
        recov = recov.replace("\\xa8", "")
        recov = recov.replace("\\x8d", "")
        recov = recov.replace("\\xa6", "")
        recov = recov.replace("\\xa6", "")
        return recov

     # METHOD TO CORRECT FOLDER NAME DIRECTLY FROM INTERNET FILES NAME(GET FILES)
    def folder_clean(self, folder):
        fold = folder.replace("?", "-").replace("=", "-").replace("%", "")
        return fold

     # METHOD TO REMOVE THE LAST DOUBLE SLASH FROM URL
    def repace_url_err(self, url):
        last_char_index = url.rfind("//")

        new_string = url[:last_char_index] + "/" + url[last_char_index+1:]
        return new_string
     # METHOD TO CHECK FILES ENDING FORMAT- REPLACE to .html or do nothing

    def endfile(self, filex):
        listf = [".php", ".aspx", ".py", ".asp", ".jsp"]
        listfiles = [".jpg", ".png", ".gif", ".pdf",
                     ".csv", ".jpeg", ".js", ".css", ".xml", ".doc", ".txt", ".pptx", ".pptm", ".ppt", ".xls", ".xlsb", ".xlsm", ".xlsx", ".docx", ".wps", ".xps"]
        a = filex.rsplit('.', 1)[-1]
        if "."+str(a) in listf:
            dlen = len(filex)
            alen = len(a)
            return filex[0:int(dlen-alen)]+"html"
        elif "."+str(a) in listfiles:
            dlen = len(filex)
            alen = len(a)
            return filex[0:]
        else:
            if ".html" in filex or ".htm" in filex:
                return filex
            else:
                return ""

    def clean_file(self, filex):
        if("?" in filex):
            a = filex.rsplit('?', 1)[-1]
            dlen = len(filex)
            alen = len(a)
            filexr = filex[0:int(dlen-alen-1)].replace("//", "/")
        else:
            filexr = filex
        return filexr

    def correct_jsurl(self, poster):
        if poster.startswith("//"):
            return "https:"+poster
        else:
            return poster

    def show_by_len(self, dlist):
        lenta = len(dlist)-1
        if lenta == 1:
            return dlist[0]
        elif lenta == 2:
            return dlist[0]+"/"+dlist[1]
        elif lenta == 3:
            return dlist[0]+"/"+dlist[1]+"/"+dlist[2]
        elif lenta == 4:
            return dlist[0]+"/"+dlist[1]+"/"+dlist[2]+"/"+dlist[3]
        elif lenta == 5:
            return dlist[0]+"/"+dlist[1]+"/"+dlist[2]+"/"+dlist[3]+"/"+dlist[4]
        elif lenta == 6:
            return dlist[0]+"/"+dlist[1]+"/"+dlist[2]+"/"+dlist[3]+"/"+dlist[4]+"/"+dlist[5]
        elif lenta == 7:
            return dlist[0]+"/"+dlist[1]+"/"+dlist[2]+"/"+dlist[3]+"/"+dlist[4]+"/"+dlist[5]+"/"+dlist[6]
        elif lenta == 8:
            return dlist[0]+"/"+dlist[1]+"/"+dlist[2]+"/"+dlist[3]+"/"+dlist[4]+"/"+dlist[5]+"/"+dlist[6]+"/"+dlist[7]
        elif lenta == 9:
            return dlist[0]+"/"+dlist[1]+"/"+dlist[2]+"/"+dlist[3]+"/"+dlist[4]+"/"+dlist[5]+"/"+dlist[6]+"/"+dlist[7]+"/"+dlist[8]
        elif lenta == 10:
            return dlist[0]+"/"+dlist[1]+"/"+dlist[2]+"/"+dlist[3]+"/"+dlist[4]+"/"+dlist[5]+"/"+dlist[6]+"/"+dlist[7]+"/"+dlist[8]+"/"+dlist[9]
        else:
            return ""

    def get_file_list(self, dlist):
        dlen = len(dlist)
        listf = dlist[dlen-1]
        return listf

    def urlactive(self, usrl):
        ua = UserAgent()
        rc = requests.get(usrl)
        prc = rc.status_code
        if prc == 200:
            return True
        else:
            return False

    def ckurl(self, url):
        if url.startswith("https://"):
            return True
        elif url.startswith("www."):
            return True
        elif url.startswith("http://"):
            return True
        elif url.startswith("//"):
            return True
        else:
            return False

    def create_folder(self, folder_name):
        if(os.path.exists(self.folder+"/"+folder_name)):
            pass
        else:
            os.makedirs(self.folder+"/"+folder_name)

    def create_file(self, file_name, content):
        try:
            if not os.path.exists(self.folder+"/"+file_name):
                # pli = open(self.folder+"/"+file_name, "wb",
                # encoding='utf-8', errors='ignore')
                with open(self.folder+"/"+file_name, 'wb') as f:
                    try:
                        f.write(content)
                        # pli.write(content)
                        print("File -"+file_name+" created in '" +
                              self.folder+"' Folder")
                        f.close()
                    except Exception as e:
                        print(e)
            else:
                print("File - " + file_name +
                      " already created in '"+self.folder+"' Folder")
        except Exception as e:
            pli = open(self.folder+"/"+file_name, "w",
                       encoding='utf-8', errors='ignore')
            pli.write(content)
            print("File -"+file_name +
                  " created as non-binary file in '"+self.folder+"' Folder")
            print(e, "create_file")

    def one_fetch(self, urltofetch, spec="none"):
        got_bad = "Got {} status code from {}"
        ua = UserAgent()
        redp = requests.get(urltofetch)
        if redp.status_code == 200:
            if spec == "none":
                print("Downloading - "+urltofetch)
            elif spec == "content":
                return(redp.content)
        else:
            print(got_bad.format(redp.status_code, urltofetch))

    def getcss(self, content):
        self.url = self.repace_url_err(self.url)
        content = content.replace(self.url+"/", "")
        soup_mysite = BeautifulSoup(content, features="lxml")
        allstylesheet = soup_mysite.findAll(
            'link', rel="stylesheet")
        description = soup_mysite.find(
            "link", {"rel": "stylesheet"})
        text = description['href']
        lister = list(allstylesheet)
        for xlist in lister:
            try:
                soup_mysitetag = BeautifulSoup(
                    str(xlist), features="lxml")
                descriptiontag = soup_mysitetag.find(
                    "link", {"rel": "stylesheet"})
                text = descriptiontag['href']
                x = re.split("\/", text)
                dlen = len(x)
                # Copy the data to anothe rlist
                xcopy = x.copy()
                # pop the last list index(the file)
                x.pop(dlen-1)
                if self.ckurl(text):
                    self.one_fetch(text)
                else:
                    self.one_fetch(self.url+"/"+text)
                    thelist = re.split(' |/|\\\\', text)
                    print("Directory:" + self.show_by_len(thelist) +
                          " Target file:"+self.get_file_list(thelist))
                    # print(thelist[0:], len(thelist))
                    self.create_folder(self.show_by_len(thelist))
                    conte = self.one_fetch(
                        self.url+"/"+text, spec="content")
                    fill = self.clean_file(text)
                    self.create_file(fill, conte)

                # print(x)
            except Exception as gr:
                print(gr, "getcss")

    def getjs(self, content):
        self.url = self.repace_url_err(self.url)
        content = content.replace(self.url+"/", "")
        # DOWNLOAD ALL JAVASCRIPT
        soup_mysitejs = BeautifulSoup(content, features="lxml")
        allstylesheetjs = soup_mysitejs.findAll(
            'script', {"src": True})
        descriptionjs = soup_mysitejs.find(
            "script", {"src": True})
        textjs = descriptionjs['src']
        listerjs = list(allstylesheetjs)
        for xlistjs in listerjs:
            try:
                soup_mysitejs = BeautifulSoup(
                    str(xlistjs), features="lxml")
                descriptiontagjs = soup_mysitejs.find(
                    "script")
                textjs = descriptiontagjs['src']
                x = re.split("\/", textjs)
                dlen = len(x)
                # Copy the data to anothe rlist
                xcopy = x.copy()
                # pop the last list index(the file)
                x.pop(dlen-1)
                if self.ckurl(textjs):
                    self.one_fetch(self.correct_jsurl(textjs))
                else:
                    self.one_fetch(self.url+"/"+textjs)
                    thelist = re.split(' |/|\\\\', textjs)
                    print("Directory:" + self.show_by_len(thelist) +
                          " Target file:"+self.get_file_list(thelist))
                    # print(thelist[0:], len(thelist))
                    self.create_folder(self.show_by_len(thelist))
                    conte = self.one_fetch(
                        self.url+"/"+textjs, spec="content")
                    fill = self.clean_file(textjs)
                    self.create_file(fill, conte)

                # print(x)
            except Exception as gr:
                print(gr, "gerjs")

    def getimg(self, content):
        self.url = self.repace_url_err(self.url)
        content = content.replace(self.url+"/", "")
        # DOWNLOAD ALL JAVASCRIPT
        soup_mysitejs = BeautifulSoup(content, features="lxml")
        allstylesheetjs = soup_mysitejs.findAll(
            'img', {"src": True})
        descriptionjs = soup_mysitejs.find(
            "img", {"src": True})
        textjs = descriptionjs['src']
        listerjs = list(allstylesheetjs)
        for xlistjs in listerjs:
            try:
                soup_mysitejs = BeautifulSoup(
                    str(xlistjs), features="lxml")
                descriptiontagjs = soup_mysitejs.find(
                    "img")
                textjs = descriptiontagjs['src']
                x = re.split("\/", textjs)
                dlen = len(x)
                # Copy the data to anothe rlist
                xcopy = x.copy()
                # pop the last list index(the file)
                x.pop(dlen-1)
                if self.ckurl(textjs):
                    self.one_fetch(self.correct_jsurl(textjs))
                else:
                    self.one_fetch(self.url+"/"+textjs)
                    thelist = re.split(' |/|\\\\', textjs)
                    print("Directory:" + self.show_by_len(thelist) +
                          " Target file:"+self.get_file_list(thelist))
                    # print(thelist[0:], len(thelist))
                    self.create_folder(self.show_by_len(thelist))
                    conte = self.one_fetch(
                        self.url+"/"+textjs, spec="content")
                    fill = self.clean_file(textjs)
                    self.create_file(fill, conte)

                # print(x)
            except Exception as gr:
                print(gr, "getimg")

    def getpages(self, content):
        self.url = self.repace_url_err(self.url)
        # DOWNLOAD ALL PAGES
        soup_mysitejs = BeautifulSoup(content, features="lxml")
        allstylesheetjs = soup_mysitejs.findAll(
            'a', {"href": True})
        descriptionjs = soup_mysitejs.find(
            "a", {"href": True})
        textjs = descriptionjs['href']
        listerjs = list(allstylesheetjs)
        for xlistjs in listerjs:
            try:
                soup_mysitejs = BeautifulSoup(
                    str(xlistjs), features="lxml")
                descriptiontagjs = soup_mysitejs.find(
                    "a")
                textjs = descriptiontagjs['href']
                x = re.split("\/", textjs)
                dlen = len(x)
                # Copy the data to another list
                xcopy = x.copy()
                # pop the last list index(the file)
                # print(self.correct_jsurl(textjs))
                x.pop(dlen-1)
                if self.ckurl(textjs):
                    if self.url+"/" in self.correct_jsurl(textjs):
                        if self.correct_jsurl(textjs) == self.url+"/":
                            print("skipping self >>")
                        else:
                            if(self.urlactive(self.correct_jsurl(textjs))):
                                self.one_fetch(self.correct_jsurl(textjs))
                                thelist = re.split(' |/|\\\\', textjs)
                                # IF href link matched self.url
                                if self.url == self.show_by_len(thelist) or self.url+"/" == self.show_by_len(thelist):
                                    resp = self.endfile(
                                        self.get_file_list(thelist))
                                    # IF it's directory
                                    if resp == "":
                                        doril = "created as folder '{}' and an index.html file"
                                        doril = doril.format(
                                            self.get_file_list(thelist))
                                        self.create_folder(
                                            self.get_file_list(thelist))
                                        conte = self.one_fetch(
                                            self.url+"/"+self.get_file_list(thelist), spec="content")
                                        try:
                                            recov = str(conte)
                                            recov3 = recov.replace(
                                                self.url+"/", "").replace(
                                                self.url, "").replace("©", "").replace("\\ue901", "")
                                            recov3 = self.smooth_replace(
                                                recov3)
                                            recov3 = self.byte_replace(recov3)
                                            print(type(recov))
                                        except TypeError as dd:
                                            print(dd, "in pages create")
                                        self.create_file(self.get_file_list(
                                            thelist)+"/index.html", recov3.encode())
                                        desclan = "direct"
                                     # If it's a file
                                    else:
                                        doril = "as file"
                                        desclan = "file"
                                        conte = self.one_fetch(
                                            self.url+"/"+self.get_file_list(thelist), spec="content")
                                        recov = str(conte)
                                        recov3 = recov.replace(
                                            self.url+"/", "").replace(
                                            self.url, "").replace("©", "").replace("\\ue901", "")
                                        recov3 = self.smooth_replace(
                                            recov3)
                                        recov3 = self.byte_replace(recov3)
                                        self.create_file(resp, recov3)
                                    print("Directory dr: default: " + self.folder + " supposed " + self.show_by_len(thelist) +
                                          " Target file dr: "+self.get_file_list(thelist)+" Final file: "+resp+" "+doril)
                                else:
                                    if self.url in self.show_by_len(thelist):
                                        resp = self.endfile(
                                            self.get_file_list(thelist))
                                        thez = re.split(
                                            ' |/|\\\\', self.show_by_len(thelist))
                                        thezlan = len(thez)
                                        if resp != "":
                                            try:
                                                self.create_folder(
                                                    str(thez[thezlan-1]))
                                                conte = self.one_fetch(
                                                    self.correct_jsurl(textjs), spec="content")
                                                recov = str(conte)
                                                recov3 = recov.replace(
                                                    self.url+"/", "").replace(
                                                    self.url, "").replace("©", "").replace("\\ue901", "")
                                                recov3 = self.smooth_replace(
                                                    recov3)
                                                recov3 = self.byte_replace(
                                                    recov3)
                                                self.create_file(self.show_by_len(thelist).replace(
                                                    self.url+"/", "")+"/"+resp, recov3)
                                            except Exception as cx:
                                                print(cx, "getpages drfall")
                                        else:
                                            print(">>Nothing downloaded")
                                            """doril = "created as folder '{}' and an index.html file"
                                            doril = doril.format(
                                                self.get_file_list(thelist))
                                            self.create_folder(
                                                self.get_file_list(thelist))
                                            conte = self.one_fetch(
                                                self.url+"/"+self.get_file_list(thelist), spec="content")
                                            print("Directory dr fall:" + self.show_by_len(thelist).replace(self.url+"/", "") +
                                                  " Target file dr fall:"+self.get_file_list(thelist)+" Final file: "+resp)"""
                                    else:
                                        print("nano")
                            else:
                                print("Cannot connect to the URL:: " +
                                      self.correct_jsurl(textjs))
                else:
                    if self.url+"/" in self.correct_jsurl(textjs):
                        if self.correct_jsurl(textjs) == self.url+"/":
                            if(self.urlactive(self.correct_jsurl(textjs))):
                                self.one_fetch(self.url+"/"+textjs)
                                thelist = re.split(' |/|\\\\', textjs)
                                print("Directory: " + self.show_by_len(thelist) +
                                      " Target file: "+self.get_file_list(thelist))
                                # print(thelist[0:], len(thelist))
                                # self.create_folder(self.show_by_len(thelist))
                                # conte = self.one_fetch(
                                # self.url+"/"+textjs, spec="content")
                                # self.create_file(textjs, conte)
                        else:
                            print("Cannot connect to the URL:: " +
                                  self.correct_jsurl(textjs))
                    else:
                        thelist = re.split(' |/|\\\\', textjs)
                        print("nn-n", self.url+"/" +
                              self.correct_jsurl(textjs), thelist)
                        doril = "created as folder '{}' and an index.html file"
                        doril = doril.format(
                            self.folder_clean(self.get_file_list(thelist)))
                        self.create_folder(
                            self.folder_clean(self.get_file_list(thelist)))
                        conte = self.one_fetch(
                            self.url+"/" +
                            self.correct_jsurl(textjs), spec="content")
                        try:
                            recov = str(conte)
                            recov3 = recov.replace(
                                self.url+"/", "").replace(
                                self.url, "").replace("©", "").replace("\\ue901", "")
                            recov3 = self.smooth_replace(
                                recov3)
                            recov3 = self.byte_replace(recov3)
                            self.create_file(self.folder_clean(self.get_file_list(
                                thelist))+"/index.html", recov3.encode())
                            print(doril)
                        except TypeError as dd:
                            print(dd, "in pages create down")

                # print(x)
            except Exception as gr:
                print(gr, "getpages")

    def start(self, srt="none"):
        try:
            if srt != "none":
                self.url = srt
            foldtxt = "Folder '{}' already exists"
            if self.ckurl(self.url):
                try:
                    ua = UserAgent()
                    req = requests.get(self.url)
                    status = req.status_code
                    content = req.content
                    content = str(content.decode('utf-8'))
                    if status == 200:
                        if(os.path.exists(self.folder)):
                            # return foldtxt.format(self.folder)
                            pass
                        else:
                            os.mkdir(self.folder)
                        # self.getjs(content)
                        try:
                            # DOWNLOAD ALL STYLESHEETS
                            self.getcss(str(content))
                            # DOWNLOAD ALL JAVASCRIPT .js FILES
                            self.getjs(str(content))
                            # DOWNLOAD ALL IMAGES <img src FILES
                            self.getimg(str(content))
                            # DOWNLOAD ALL PAGES IN INDEX
                            self.getpages(
                                str(content))
                            # DOWNLOAD INDEX.HTML FILE
                            # modify the links inside file
                            recov = str(content).replace(self.url, "")
                            recov = str(content.replace(
                                self.url+"/", "").replace(
                                self.url, "").replace("©", "").replace("\\ue901", ""))
                            recov = self.smooth_replace(recov)
                            self.create_file("index.html", recov.encode())
                            print(">>> Clone completed <<< - Check " +
                                  self.folder+" Folder")
                        except Exception as ex:
                            print(ex, "start clone")

                    else:
                        return ">>> Website is not reachable <<<"
                except Exception as dclass:
                    print(dclass)
            else:
                print(">>> Url is invalid <<<")
        except Exception as nv:
            print(nv, "start main")


de = cloner(input("Insert the web URL: "), input("Insert directory name: "))
de.start()

