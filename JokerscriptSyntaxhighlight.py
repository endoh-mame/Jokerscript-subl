import sublime, sublime_plugin

import os, sys

# コメントアウトコマンド
class JokerscriptCommentCommand(sublime_plugin.TextCommand):
	
	# def testDef(self, evt):
	# 	print('evt', evt)

	def run(self, edit):
		# sublime.active_window().create_output_panel('aaa')
		# sublime.active_window().show_quick_panel(['a', 'b'], self.testDef)
		# print(self.view.settings().get('syntax'))
		# syntaxFile = 'Packages/Jokerscript-subl/.TXT-tmLanguage.tmLanguage'
		# self.view.set_syntax_file(syntaxFile)
		# ポップアップテスト
		# self.view.show_popup_menu(['a', 'b'], self.testDef);

		# 拡張子が.txtなら
		splitext = os.path.splitext(self.view.file_name())[1]
		if splitext == '.txt':
			self.commentOut(edit, self.view.sel())
		else:
			self.view.run_command('toggle_comment')

	# コメントアウト関数
	# (コメントアウトされている場合はコメントアウト解除)
	def commentOut(self, edit, selection):
		# TODO
		for s in selection:
			regs = self.view.lines(s)
			isCommented = False
			for reg in regs:
				l = self.view.substr(self.view.line(reg))
				if len(l) != 0:
					isCommented = l[0] is ';'
			print(isCommented)

			if isCommented:
				# すでにコメントアウトされていたら
				for region in selection:
					linesReg = self.view.lines(region)
					count = 0
					for lr in linesReg:
						eraseReg = sublime.Region(lr.begin() - count, lr.begin()+1-count)
						self.view.erase(edit, eraseReg)
						count += 1
			else:
				# コメントアウトされていなかったら
				for region in selection:
					start_point = region.begin()
					end_point = region.end()
					start_row, _ = self.view.rowcol(start_point)
					end_row, end_col = self.view.rowcol(end_point)
					if end_col == 0 :
						end_row = end_row - 1
					for row in range(start_row, end_row + 1):
						self.view.insert(edit, self.view.text_point(row, 0), ";")

# MEMO: 実行
# view.run_command('jokerscript_syntaxhighlight')

# オンオフ切り替え
class JokerscriptSublCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		settings = sublime.load_settings('JokerscriptSubl.sublime-settings')
		settings.set('isComplete', not settings.get('isComplete'))
		isComplete = settings.get('isComplete')

# 自動補完
class CompleteJoker(sublime_plugin.EventListener):
	def on_query_completions(self, view, prefix, locations):
		settings = sublime.load_settings('JokerscriptSubl.sublime-settings')
		isComplete = settings.get('isComplete')
		if isComplete:
			return[
			('playbgm','playbgm'),
			('stopbgm','stopbgm'),
			('playse','playse'),
			('stopse','stopse'),
			('bg_new','bg_new'),
			('bg_show','bg_show'),
			('bg_hide','bg_hide'),
			('bg_remove','bg_remove'),
			('show','show'),
			('hide','hide'),
			('remove','remove'),
			('image_new','image_new'),
			('image_pos','image_pos'),
			('image_show','image_show'),
			('image_hide','image_hide'),
			('image_face','image_face'),
			('image_mod','image_mod'),
			('image_remove','image_remove'),
			('button_new','button_new'),
			('button_pos','button_pos'),
			('button_show','button_show'),
			('button_hide','button_hide'),
			('button_mod','button_mod'),
			('button_remove','button_remove'),
			('chara_new','chara_new'),
			('chara_pos','chara_pos'),
			('chara_show','chara_show'),
			('chara_hide','chara_hide'),
			('chara_face','chara_face'),
			('chara_mod','chara_mod'),
			('chara_remove','chara_remove'),
			('clickable','clickable'),
			('story','story'),
			('r','r'),
			('l','l'),
			('p','p'),
			('cm','cm'),
			('delay','delay'),
			('font','font'),
			('fontreset','fontreset'),
			('emb','emb'),
			('evt','evt'),
			('evt_remove','evt_remove'),
			('evt_stop','evt_stop'),
			('evt_resume','evt_resume'),
			('live2d_new','live2d_new'),
			('live2d_pos','live2d_pos'),
			('live2d_show','live2d_show'),
			('live2d_hide','live2d_hide'),
			('live2d_remove','live2d_remove'),
			('live2d_motion','live2d_motion'),
			('skipstart','skipstart'),
			('skipstop','skipstop'),
			('savesnap','savesnap'),
			('sleepgame','sleepgame'),
			('awakegame','awakegame'),
			('autostart','autostart'),
			('save','save'),
			('load','load'),
			('saveloop','saveloop'),
			('end_saveloop','end_saveloop'),
			('autosave','autosave'),
			('get_autosave','get_autosave'),
			('sd_new','sd_new'),
			('sd_show','sd_show'),
			('sd_remove','sd_remove'),
			('sd_hide','sd_hide'),
			('sd_anim','sd_anim'),
			('macro','macro'),
			('endmacro','endmacro'),
			('jump','jump'),
			('call','call'),
			('return','return'),
			('calc','calc'),
			('flag','flag'),
			('hidemessage','hidemessage'),
			('showmessage','showmessage'),
			('trace','trace'),
			('talk_name','talk_name'),
			('wait','wait'),
			('clearvar','clearvar'),
			('showlog','showlog'),
			('if','if'),
			('elsif','elsif'),
			('else','else'),
			('endif','endif'),
			('s','s'),
			('tag_default','tag_default'),
			('reset_tag_default','reset_tag_default'),
			('web','web'),
			('text_new','text_new'),
			('image_pos','image_pos'),
			('text_show','text_show'),
			('text_hide','text_hide'),
			('text_mod','text_mod'),
			('text_remove','text_remove'),
			('name','name'),
			('tag','tag'),
			('time','time'),
			('type','type'),
			('wait','wait'),
			('x','x'),
			('y','y'),
			('scale','scale'),
			('storage','storage'),
			('vol','vol'),
			('next','next'),
			('loop','loop'),
			('layer','layer'),
			('sort','sort'),
			('scale_x','scale_x'),
			('scale_y','scale_y'),
			('LowerCenter','LowerCenter'),
			('LowerLeft','LowerLeft'),
			('LowerRight','LowerRight'),
			('MiddleCenter','MiddleCenter'),
			('MiddleLeft','MiddleLeft'),
			('MiddleRight','MiddleRight'),
			('UpperCenter','UpperCenter'),
			('UpperLeft','UpperLeft'),
			('UpperRight','UpperRight'),
			('MiddleCenter','MiddleCenter'),
			('width','width'),
			('scale','scale'),
			('anchor','anchor'),
			('color','color'),
			('fontsize','fontsize'),
			('cut','cut'),
			('jname','jname'),
			('jcolor','jcolor'),
			('scale_x','scale_x'),
			('scale_y','scale_y'),
			('scale_z','scale_z'),
			('face','face'),
			('val','val'),
			('act','act'),
			('file','file'),
			('target','target'),
			('speed','speed'),
			('num','num'),
			('page','page'),
			('rot_x','rot_x'),
			('rot_y','rot_y'),
			('rot_z','rot_z'),
			('state','state'),
			('condition','condition'),
			('index','index'),
			('exp','exp'),
			('url','url'),
			('LowerCenter','LowerCenter'),
			('LowerLeft','LowerLeft'),
			('LowerRight','LowerRight'),
			('MiddleCenter','MiddleCenter'),
			('MiddleLeft','MiddleLeft'),
			('MiddleRight','MiddleRight'),
			('UpperCenter','UpperCenter'),
			('UpperLeft','UpperLeft'),
			('UpperRight','UpperRight'),
			('MiddleCenter','MiddleCenter'),
			('Left','Left'),
			('Right','Right'),
			('Center','Center')
			]
		

