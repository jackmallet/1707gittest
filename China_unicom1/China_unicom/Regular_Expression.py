regularExpression = r'<STRONG.*?>|</STRONG>|<strong.*?>|</strong>|<SPAN.*?>|</SPAN>|<span.*?>|</span>|<FONT.*?>|</FONT>|<font.*?>|</font>|<meta.*?/>|<input.*?>|<INPUT.*?>|<head.*>.*?</head>|<HEAD.*>.*?</HEAD>|<!DOCTYPE.*?>|<STYLE.*?</STYLE>|<style.*?</style>|&nbsp;|<o:p>|</o:p>|<!--.*?-->|<LINK.*?>|<link.*?>|<html.*?>|</html>|<HTML.*?>|</HTML>|<body.*?>|</body>|<BODY.*?>|</BODY>|class\s*=\s*[\"\'].*?[\"\']|CLASS\s*=\s*[\"\'].*?[\"\']|id\s*=\s*[\"\'].*?[\"\']|ID\s*=\s*[\"\'].*?[\"\']|name\s*=\s*[\"\'].*?[\"\']|NAME\s*=\s*[\"\'].*?[\"\']|STYLE\s*=.?[\'\"].*?[\'\"]|style\s*=.?[\'\"].*?[\'\"]|\r|\t|\n|lang=[\'\"].*?[\'\"]|"MsoNorma"'

# 眉山市
regularExpression02 = r'\sstyle=.*?>'


category = {
            '招标公告' : '38255',
            '变更公告' : '38256',
            '招标结果' : '38257',
            '招标预告' : '38254',
            '招标更正' : '38256',
        }

wukuang_regularExpression = r'\r|\t|\n|\s|<o:p>|</o:p>|<!--.*?>.*?<!.*?>|<!--.*?>|id=[\w\s]+?|class=[\w\s]+?|<input.*?>|style=[\'].*?[\']|style=[\"].*?[\"]|id=[\'\"].*?[\'\"]|class=[\'\"].*?[\'\"]|class\s*\'*\"*=\s*[a-zA-Z0-9_]*\'*\"*|<script.*?</script>|<style.*?</style>|<STYLE.*?</STYLE>|lang=[\'\"].*?[\'\"]|name=[\'\"].*?[\'\"]|<font.*?>|&nbsp;|<style.*?>|<head.*>.*?</head>|<!DOCTYPE.*?>|<HEAD.*>.*?</HEAD>'

chinaRailway_summary_regularExpression = r'\r|\t|\n|\s|<o:p>|</o:p>|<!--.*?>.*?<!.*?>|<!--.*?>|class=[\w\s]+?|<input.*?>|style=[\'].*?[\']|style=[\"].*?[\"]|class=[\'\"].*?[\'\"]|class\s*\'*\"*=\s*[a-zA-Z0-9_]*\'*\"*|<script.*?</script>|<style.*?</style>|<STYLE.*?</STYLE>|lang=[\'\"].*?[\'\"]|name=[\'\"].*?[\'\"]|<font.*?>|&nbsp;|<style.*?>|onclick=\".*?\"|onclick=\'.*?\'|<head.*>.*?</head>|<!DOCTYPE.*?>|<HEAD.*>.*?</HEAD>'

# '''<span style="font-family:'Times New Roman','serif';font-size:10.5pt;">''' 难题

# 中国招标投标公共服务平台拼接url
html_tag = '<a id="viewerPlaceHolder" style="width: 100%; height: 660px; display: block"><object width="100%" height="100%" id="_4417482512" name="_4417482512" data="http://bulletin.cebpubservice.com/FlexPaperViewer.swf" type="application/x-shockwave-flash"><param name="allowfullscreen" value="true"><param name="allowscriptaccess" value="always"><param name="quality" value="high"><param name="flashvars" value="SwfFile={}&Scale=0.6&ZoomTransition=easeOut&ZoomTime=0.5&ZoomInterval=0.05&FitPageOnLoad=true&FitWidthOnLoad=true&ProgressiveLoading=true&MinZoomSize=0.05&MaxZoomSize=5&InitViewMode=Portrait&ViewModeToolsVisible=true&ZoomToolsVisible=true&NavToolsVisible=true&CursorToolsVisible=true&localeChain=zh_CN"><param name="wmode" value="transparent"></object></a>'