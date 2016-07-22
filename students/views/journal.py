# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

#Views for journal
def journal_list(request):
	students = (
	{'id': 1,
	'name': u'Бабін Владислав'},
	{'id': 2,
	'name': u'Ткач Віктор'},
	{'id': 3,
	'name': u'Медведев Дмитро'},
	)
	return render (request, 'students/journal_list.html',
	{'students': students})

def journal_edit(request, jid):
	return HttpResponse('<h1>Journal edit %s</h1>' % jid)