
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">

<html>
<head>
	<title>$page.title</title>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>
<body>
<div>

#for $predecessor in $page.get_predecessors()
<a href="$predecessor.get_alternative_path_to($page)">$predecessor.title</a> -> 
#end for
$page.title
</div>
<div>
<h2>$page.title</h2>
<br/>
$page.content
</div>

<div>
<table>
#for $file in $page.attachments
<tr>
<td><a href="$file.name">$file.name</a></td>
<td>$file.summary</td>
<td>$file.author.name</td>
<td><a href="mailto:$file.author.email">$file.author.email</a></td>
<td>$file.updated.en</td>
<td>$file.revision</td>
</tr>
#end for

#for $file in $page.web_attachments
<tr>
<td><a href="$file.web_src">$file.name</a></td>
<td>$file.summary</td>
<td>$file.author.name</td>
<td><a href="mailto:$file.author.email">$file.author.email</a></td>
<td>$file.updated.en</td>
<td>$file.revision</td>
</tr>
#end for

</table>
</div>


<div>
<hr/>
<h3>Subpages</h3>
#for $child in $page.childs
<a href="$child.subpage_path">$child.title</a><br/>
#end for
</div>


#if $page.comments
<div>
<hr/>
<h3>Comments</h3>
<table>
#for $comment in $page.comments
<tr>
<td>
$comment.author.name, $comment.author.email, $comment.updated.en, revision: $comment.revision
<p>
$comment.text
</p>
</td>
</tr>
#end for
</table>
</div>
#end if


<hr/>
<div>
author: $page.author.name, $page.author.email<br/>
updated: $page.updated.cz<br/>
revision: $page.revision
</div>

</body>
</html>



