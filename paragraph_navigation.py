import sublime
import sublime_plugin
import re
import datetime

class MoveByParagraphCommand(sublime_plugin.TextCommand):
  
  def run(self, edit, extend=False, forward=False, by="paragraphs"):

    selection = self.view.sel()

    for region in selection:

      start_point = region.b()
      end_point = start_point

      
      #if forward:
      #  end_point = self.view.find_by_class( end_point, forward, sublime.CLASS_)
      #  if self.view.classify(end_point) & sublime.CLASS_EMPTY_LINE:
      #    end_point = self.view.find_by_class( end_point, forward, 
      #  self.view.sel().clear()
      #  self.view.sel().add(sublime.Region(start_point, end_point))
        
        
      #start_point = self.view.find_by_class( region.begin(), False, sublime.CLASS_LINE_END|sublime.CLASS_EMPTY_LINE)
      #print("region: " + str(region))
      #print("start point: " + str(start_point))
      #self.view.sel().clear()
      #self.view.sel().add( sublime.Region(start_point, region.end()))

    
