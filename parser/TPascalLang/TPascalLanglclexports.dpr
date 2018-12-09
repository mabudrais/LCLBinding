library lclexports;
uses classes,sysutils,types,typinfo,math,custapp,lclstrconsts,lclversion,lcltype,lclclasses,lresources,graphics,menus,lmessages,customtimer,actnlist,clipbrd,helpintfs,controls,imglist,themes,lazfileutils,lazutf8,maps,gettext;
//745
function Forms_tform_create( theowner:Pointer):Pointer;cdecl;
begin
Result:=Pointer(tform.create(theowner));
end;
//Forms tform lclversion 842
function Forms_tform_lclversion_set(controlpointer:Pointer;p:PChar);cdecl;
begin
tform(controlpointer).lclversion:=p;
end;
//Forms tform lclversion 842
function Forms_tform_lclversion_get(controlpointer:Pointer);cdecl;
begin
Result:=PChar(tform(controlpointer).lclversion);
end;
//Forms tcustomform clienthandle 606
function Forms_tcustomform_clienthandle_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).clienthandle);
end;
//608
function Forms_tcustomform_create( aowner:Pointer):Pointer;cdecl;
begin
Result:=Pointer(tcustomform.create(aowner));
end;
//609
function Forms_tcustomform_createnew( aowner:Pointer; num:Integer):Pointer;cdecl;
begin
Result:=Pointer(tcustomform.createnew(aowner,num));
end;
//Forms tcustomform active 671
function Forms_tcustomform_active_get(controlpointer:Pointer);cdecl;
begin
Result:=Boolean(tcustomform(controlpointer).active);
end;
//Forms tcustomform activecontrol 672
function Forms_tcustomform_activecontrol_set(controlpointer:Pointer;p:Pointer);cdecl;
begin
tcustomform(controlpointer).activecontrol:=p;
end;
//Forms tcustomform activecontrol 672
function Forms_tcustomform_activecontrol_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).activecontrol);
end;
//Forms tcustomform activedefaultcontrol 673
function Forms_tcustomform_activedefaultcontrol_set(controlpointer:Pointer;p:Pointer);cdecl;
begin
tcustomform(controlpointer).activedefaultcontrol:=p;
end;
//Forms tcustomform activedefaultcontrol 673
function Forms_tcustomform_activedefaultcontrol_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).activedefaultcontrol);
end;
//Forms tcustomform allowdropfiles 674
function Forms_tcustomform_allowdropfiles_set(controlpointer:Pointer;p:Boolean);cdecl;
begin
tcustomform(controlpointer).allowdropfiles:=p;
end;
//Forms tcustomform allowdropfiles 674
function Forms_tcustomform_allowdropfiles_get(controlpointer:Pointer);cdecl;
begin
Result:=Boolean(tcustomform(controlpointer).allowdropfiles);
end;
//Forms tcustomform alphablend 675
function Forms_tcustomform_alphablend_set(controlpointer:Pointer;p:Boolean);cdecl;
begin
tcustomform(controlpointer).alphablend:=p;
end;
//Forms tcustomform alphablend 675
function Forms_tcustomform_alphablend_get(controlpointer:Pointer);cdecl;
begin
Result:=Boolean(tcustomform(controlpointer).alphablend);
end;
//Forms tcustomform alphablendvalue 676
function Forms_tcustomform_alphablendvalue_set(controlpointer:Pointer;p:Pointer);cdecl;
begin
tcustomform(controlpointer).alphablendvalue:=p;
end;
//Forms tcustomform alphablendvalue 676
function Forms_tcustomform_alphablendvalue_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).alphablendvalue);
end;
//Forms tcustomform bordericons 678
function Forms_tcustomform_bordericons_set(controlpointer:Pointer;p:Pointer);cdecl;
begin
tcustomform(controlpointer).bordericons:=p;
end;
//Forms tcustomform bordericons 678
function Forms_tcustomform_bordericons_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).bordericons);
end;
//Forms tcustomform borderstyle 680
function Forms_tcustomform_borderstyle_set(controlpointer:Pointer;p:Pointer);cdecl;
begin
tcustomform(controlpointer).borderstyle:=p;
end;
//Forms tcustomform borderstyle 680
function Forms_tcustomform_borderstyle_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).borderstyle);
end;
//Forms tcustomform cancelcontrol 682
function Forms_tcustomform_cancelcontrol_set(controlpointer:Pointer;p:Pointer);cdecl;
begin
tcustomform(controlpointer).cancelcontrol:=p;
end;
//Forms tcustomform cancelcontrol 682
function Forms_tcustomform_cancelcontrol_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).cancelcontrol);
end;
//Forms tcustomform defaultcontrol 685
function Forms_tcustomform_defaultcontrol_set(controlpointer:Pointer;p:Pointer);cdecl;
begin
tcustomform(controlpointer).defaultcontrol:=p;
end;
//Forms tcustomform defaultcontrol 685
function Forms_tcustomform_defaultcontrol_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).defaultcontrol);
end;
//Forms tcustomform defaultmonitor 686
function Forms_tcustomform_defaultmonitor_set(controlpointer:Pointer;p:Pointer);cdecl;
begin
tcustomform(controlpointer).defaultmonitor:=p;
end;
//Forms tcustomform defaultmonitor 686
function Forms_tcustomform_defaultmonitor_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).defaultmonitor);
end;
//Forms tcustomform designer 688
function Forms_tcustomform_designer_set(controlpointer:Pointer;p:Pointer);cdecl;
begin
tcustomform(controlpointer).designer:=p;
end;
//Forms tcustomform designer 688
function Forms_tcustomform_designer_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).designer);
end;
//Forms tcustomform effectiveshowintaskbar 689
function Forms_tcustomform_effectiveshowintaskbar_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).effectiveshowintaskbar);
end;
//Forms tcustomform formstate 690
function Forms_tcustomform_formstate_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).formstate);
end;
//Forms tcustomform formstyle 691
function Forms_tcustomform_formstyle_set(controlpointer:Pointer;p:Pointer);cdecl;
begin
tcustomform(controlpointer).formstyle:=p;
end;
//Forms tcustomform formstyle 691
function Forms_tcustomform_formstyle_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).formstyle);
end;
//Forms tcustomform helpfile 693
function Forms_tcustomform_helpfile_set(controlpointer:Pointer;p:PChar);cdecl;
begin
tcustomform(controlpointer).helpfile:=p;
end;
//Forms tcustomform helpfile 693
function Forms_tcustomform_helpfile_get(controlpointer:Pointer);cdecl;
begin
Result:=PChar(tcustomform(controlpointer).helpfile);
end;
//Forms tcustomform icon 694
function Forms_tcustomform_icon_set(controlpointer:Pointer;p:Pointer);cdecl;
begin
tcustomform(controlpointer).icon:=p;
end;
//Forms tcustomform icon 694
function Forms_tcustomform_icon_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).icon);
end;
//Forms tcustomform keypreview 695
function Forms_tcustomform_keypreview_set(controlpointer:Pointer;p:Boolean);cdecl;
begin
tcustomform(controlpointer).keypreview:=p;
end;
//Forms tcustomform keypreview 695
function Forms_tcustomform_keypreview_get(controlpointer:Pointer);cdecl;
begin
Result:=Boolean(tcustomform(controlpointer).keypreview);
end;
//Forms tcustomform menu 697
function Forms_tcustomform_menu_set(controlpointer:Pointer;p:Pointer);cdecl;
begin
tcustomform(controlpointer).menu:=p;
end;
//Forms tcustomform menu 697
function Forms_tcustomform_menu_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).menu);
end;
//Forms tcustomform modalresult 698
function Forms_tcustomform_modalresult_set(controlpointer:Pointer;p:Pointer);cdecl;
begin
tcustomform(controlpointer).modalresult:=p;
end;
//Forms tcustomform modalresult 698
function Forms_tcustomform_modalresult_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).modalresult);
end;
//Forms tcustomform monitor 699
function Forms_tcustomform_monitor_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).monitor);
end;
//Forms tcustomform popupmode 700
function Forms_tcustomform_popupmode_set(controlpointer:Pointer;p:Pointer);cdecl;
begin
tcustomform(controlpointer).popupmode:=p;
end;
//Forms tcustomform popupmode 700
function Forms_tcustomform_popupmode_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).popupmode);
end;
//Forms tcustomform popupparent 701
function Forms_tcustomform_popupparent_set(controlpointer:Pointer;p:Pointer);cdecl;
begin
tcustomform(controlpointer).popupparent:=p;
end;
//Forms tcustomform popupparent 701
function Forms_tcustomform_popupparent_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).popupparent);
end;
//Forms tcustomform onactivate 703
function Forms_tcustomform_onactivate_set(controlpointer:Pointer;p:Pointer);cdecl;
begin
tcustomform(controlpointer).onactivate:=p;
end;
//Forms tcustomform onactivate 703
function Forms_tcustomform_onactivate_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).onactivate);
end;
//Forms tcustomform onclose 704
function Forms_tcustomform_onclose_set(controlpointer:Pointer;p:Pointer);cdecl;
begin
tcustomform(controlpointer).onclose:=p;
end;
//Forms tcustomform onclose 704
function Forms_tcustomform_onclose_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).onclose);
end;
//Forms tcustomform onclosequery 705
function Forms_tcustomform_onclosequery_set(controlpointer:Pointer;p:Pointer);cdecl;
begin
tcustomform(controlpointer).onclosequery:=p;
end;
//Forms tcustomform onclosequery 705
function Forms_tcustomform_onclosequery_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).onclosequery);
end;
//Forms tcustomform oncreate 707
function Forms_tcustomform_oncreate_set(controlpointer:Pointer;p:Pointer);cdecl;
begin
tcustomform(controlpointer).oncreate:=p;
end;
//Forms tcustomform oncreate 707
function Forms_tcustomform_oncreate_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).oncreate);
end;
//Forms tcustomform ondeactivate 708
function Forms_tcustomform_ondeactivate_set(controlpointer:Pointer;p:Pointer);cdecl;
begin
tcustomform(controlpointer).ondeactivate:=p;
end;
//Forms tcustomform ondeactivate 708
function Forms_tcustomform_ondeactivate_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).ondeactivate);
end;
//Forms tcustomform ondestroy 709
function Forms_tcustomform_ondestroy_set(controlpointer:Pointer;p:Pointer);cdecl;
begin
tcustomform(controlpointer).ondestroy:=p;
end;
//Forms tcustomform ondestroy 709
function Forms_tcustomform_ondestroy_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).ondestroy);
end;
//Forms tcustomform ondropfiles 710
function Forms_tcustomform_ondropfiles_set(controlpointer:Pointer;p:Pointer);cdecl;
begin
tcustomform(controlpointer).ondropfiles:=p;
end;
//Forms tcustomform ondropfiles 710
function Forms_tcustomform_ondropfiles_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).ondropfiles);
end;
//Forms tcustomform onhelp 711
function Forms_tcustomform_onhelp_set(controlpointer:Pointer;p:Pointer);cdecl;
begin
tcustomform(controlpointer).onhelp:=p;
end;
//Forms tcustomform onhelp 711
function Forms_tcustomform_onhelp_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).onhelp);
end;
//Forms tcustomform onhide 712
function Forms_tcustomform_onhide_set(controlpointer:Pointer;p:Pointer);cdecl;
begin
tcustomform(controlpointer).onhide:=p;
end;
//Forms tcustomform onhide 712
function Forms_tcustomform_onhide_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).onhide);
end;
//Forms tcustomform onshortcut 714
function Forms_tcustomform_onshortcut_set(controlpointer:Pointer;p:Pointer);cdecl;
begin
tcustomform(controlpointer).onshortcut:=p;
end;
//Forms tcustomform onshortcut 714
function Forms_tcustomform_onshortcut_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).onshortcut);
end;
//Forms tcustomform onshow 715
function Forms_tcustomform_onshow_set(controlpointer:Pointer;p:Pointer);cdecl;
begin
tcustomform(controlpointer).onshow:=p;
end;
//Forms tcustomform onshow 715
function Forms_tcustomform_onshow_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).onshow);
end;
//Forms tcustomform onshowmodalfinished 716
function Forms_tcustomform_onshowmodalfinished_set(controlpointer:Pointer;p:Pointer);cdecl;
begin
tcustomform(controlpointer).onshowmodalfinished:=p;
end;
//Forms tcustomform onshowmodalfinished 716
function Forms_tcustomform_onshowmodalfinished_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).onshowmodalfinished);
end;
//Forms tcustomform onwindowstatechange 717
function Forms_tcustomform_onwindowstatechange_set(controlpointer:Pointer;p:Pointer);cdecl;
begin
tcustomform(controlpointer).onwindowstatechange:=p;
end;
//Forms tcustomform onwindowstatechange 717
function Forms_tcustomform_onwindowstatechange_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).onwindowstatechange);
end;
//Forms tcustomform position 720
function Forms_tcustomform_position_set(controlpointer:Pointer;p:Pointer);cdecl;
begin
tcustomform(controlpointer).position:=p;
end;
//Forms tcustomform position 720
function Forms_tcustomform_position_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).position);
end;
//Forms tcustomform restoredleft 721
function Forms_tcustomform_restoredleft_get(controlpointer:Pointer);cdecl;
begin
Result:=Integer(tcustomform(controlpointer).restoredleft);
end;
//Forms tcustomform restoredtop 722
function Forms_tcustomform_restoredtop_get(controlpointer:Pointer);cdecl;
begin
Result:=Integer(tcustomform(controlpointer).restoredtop);
end;
//Forms tcustomform restoredwidth 723
function Forms_tcustomform_restoredwidth_get(controlpointer:Pointer);cdecl;
begin
Result:=Integer(tcustomform(controlpointer).restoredwidth);
end;
//Forms tcustomform restoredheight 724
function Forms_tcustomform_restoredheight_get(controlpointer:Pointer);cdecl;
begin
Result:=Integer(tcustomform(controlpointer).restoredheight);
end;
//Forms tcustomform showintaskbar 725
function Forms_tcustomform_showintaskbar_set(controlpointer:Pointer;p:Pointer);cdecl;
begin
tcustomform(controlpointer).showintaskbar:=p;
end;
//Forms tcustomform showintaskbar 725
function Forms_tcustomform_showintaskbar_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).showintaskbar);
end;
//Forms tcustomform windowstate 728
function Forms_tcustomform_windowstate_set(controlpointer:Pointer;p:Pointer);cdecl;
begin
tcustomform(controlpointer).windowstate:=p;
end;
//Forms tcustomform windowstate 728
function Forms_tcustomform_windowstate_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tcustomform(controlpointer).windowstate);
end;
//274
function Forms_tcustomdesigncontrol_create( theowner:Pointer):Pointer;cdecl;
begin
Result:=Pointer(tcustomdesigncontrol.create(theowner));
end;
//Forms tcustomdesigncontrol designtimeppi 276
function Forms_tcustomdesigncontrol_designtimeppi_set(controlpointer:Pointer;p:Integer);cdecl;
begin
tcustomdesigncontrol(controlpointer).designtimeppi:=p;
end;
//Forms tcustomdesigncontrol designtimeppi 276
function Forms_tcustomdesigncontrol_designtimeppi_get(controlpointer:Pointer);cdecl;
begin
Result:=Integer(tcustomdesigncontrol(controlpointer).designtimeppi);
end;
//Forms tcustomdesigncontrol pixelsperinch 277
function Forms_tcustomdesigncontrol_pixelsperinch_set(controlpointer:Pointer;p:Integer);cdecl;
begin
tcustomdesigncontrol(controlpointer).pixelsperinch:=p;
end;
//Forms tcustomdesigncontrol pixelsperinch 277
function Forms_tcustomdesigncontrol_pixelsperinch_get(controlpointer:Pointer);cdecl;
begin
Result:=Integer(tcustomdesigncontrol(controlpointer).pixelsperinch);
end;
//Forms tcustomdesigncontrol scaled 278
function Forms_tcustomdesigncontrol_scaled_set(controlpointer:Pointer;p:Boolean);cdecl;
begin
tcustomdesigncontrol(controlpointer).scaled:=p;
end;
//Forms tcustomdesigncontrol scaled 278
function Forms_tcustomdesigncontrol_scaled_get(controlpointer:Pointer);cdecl;
begin
Result:=Boolean(tcustomdesigncontrol(controlpointer).scaled);
end;
//Forms tscrollingwincontrol autoscroll 179
function Forms_tscrollingwincontrol_autoscroll_set(controlpointer:Pointer;p:Boolean);cdecl;
begin
tscrollingwincontrol(controlpointer).autoscroll:=p;
end;
//Forms tscrollingwincontrol autoscroll 179
function Forms_tscrollingwincontrol_autoscroll_get(controlpointer:Pointer);cdecl;
begin
Result:=Boolean(tscrollingwincontrol(controlpointer).autoscroll);
end;
//182
function Forms_tscrollingwincontrol_create( theowner:Pointer):Pointer;cdecl;
begin
Result:=Pointer(tscrollingwincontrol.create(theowner));
end;
//Forms tscrollingwincontrol horzscrollbar 189
function Forms_tscrollingwincontrol_horzscrollbar_set(controlpointer:Pointer;p:Pointer);cdecl;
begin
tscrollingwincontrol(controlpointer).horzscrollbar:=p;
end;
//Forms tscrollingwincontrol horzscrollbar 189
function Forms_tscrollingwincontrol_horzscrollbar_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tscrollingwincontrol(controlpointer).horzscrollbar);
end;
//Forms tscrollingwincontrol vertscrollbar 190
function Forms_tscrollingwincontrol_vertscrollbar_set(controlpointer:Pointer;p:Pointer);cdecl;
begin
tscrollingwincontrol(controlpointer).vertscrollbar:=p;
end;
//Forms tscrollingwincontrol vertscrollbar 190
function Forms_tscrollingwincontrol_vertscrollbar_get(controlpointer:Pointer);cdecl;
begin
Result:=Pointer(tscrollingwincontrol(controlpointer).vertscrollbar);
end;
exports
Forms_tform_create
,Forms_tform_lclversion_set
,Forms_tform_lclversion_get
,Forms_tcustomform_clienthandle_get
,Forms_tcustomform_create
,Forms_tcustomform_createnew
,Forms_tcustomform_active_get
,Forms_tcustomform_activecontrol_set
,Forms_tcustomform_activecontrol_get
,Forms_tcustomform_activedefaultcontrol_set
,Forms_tcustomform_activedefaultcontrol_get
,Forms_tcustomform_allowdropfiles_set
,Forms_tcustomform_allowdropfiles_get
,Forms_tcustomform_alphablend_set
,Forms_tcustomform_alphablend_get
,Forms_tcustomform_alphablendvalue_set
,Forms_tcustomform_alphablendvalue_get
,Forms_tcustomform_bordericons_set
,Forms_tcustomform_bordericons_get
,Forms_tcustomform_borderstyle_set
,Forms_tcustomform_borderstyle_get
,Forms_tcustomform_cancelcontrol_set
,Forms_tcustomform_cancelcontrol_get
,Forms_tcustomform_defaultcontrol_set
,Forms_tcustomform_defaultcontrol_get
,Forms_tcustomform_defaultmonitor_set
,Forms_tcustomform_defaultmonitor_get
,Forms_tcustomform_designer_set
,Forms_tcustomform_designer_get
,Forms_tcustomform_effectiveshowintaskbar_get
,Forms_tcustomform_formstate_get
,Forms_tcustomform_formstyle_set
,Forms_tcustomform_formstyle_get
,Forms_tcustomform_helpfile_set
,Forms_tcustomform_helpfile_get
,Forms_tcustomform_icon_set
,Forms_tcustomform_icon_get
,Forms_tcustomform_keypreview_set
,Forms_tcustomform_keypreview_get
,Forms_tcustomform_menu_set
,Forms_tcustomform_menu_get
,Forms_tcustomform_modalresult_set
,Forms_tcustomform_modalresult_get
,Forms_tcustomform_monitor_get
,Forms_tcustomform_popupmode_set
,Forms_tcustomform_popupmode_get
,Forms_tcustomform_popupparent_set
,Forms_tcustomform_popupparent_get
,Forms_tcustomform_onactivate_set
,Forms_tcustomform_onactivate_get
,Forms_tcustomform_onclose_set
,Forms_tcustomform_onclose_get
,Forms_tcustomform_onclosequery_set
,Forms_tcustomform_onclosequery_get
,Forms_tcustomform_oncreate_set
,Forms_tcustomform_oncreate_get
,Forms_tcustomform_ondeactivate_set
,Forms_tcustomform_ondeactivate_get
,Forms_tcustomform_ondestroy_set
,Forms_tcustomform_ondestroy_get
,Forms_tcustomform_ondropfiles_set
,Forms_tcustomform_ondropfiles_get
,Forms_tcustomform_onhelp_set
,Forms_tcustomform_onhelp_get
,Forms_tcustomform_onhide_set
,Forms_tcustomform_onhide_get
,Forms_tcustomform_onshortcut_set
,Forms_tcustomform_onshortcut_get
,Forms_tcustomform_onshow_set
,Forms_tcustomform_onshow_get
,Forms_tcustomform_onshowmodalfinished_set
,Forms_tcustomform_onshowmodalfinished_get
,Forms_tcustomform_onwindowstatechange_set
,Forms_tcustomform_onwindowstatechange_get
,Forms_tcustomform_position_set
,Forms_tcustomform_position_get
,Forms_tcustomform_restoredleft_get
,Forms_tcustomform_restoredtop_get
,Forms_tcustomform_restoredwidth_get
,Forms_tcustomform_restoredheight_get
,Forms_tcustomform_showintaskbar_set
,Forms_tcustomform_showintaskbar_get
,Forms_tcustomform_windowstate_set
,Forms_tcustomform_windowstate_get
,Forms_tcustomdesigncontrol_create
,Forms_tcustomdesigncontrol_designtimeppi_set
,Forms_tcustomdesigncontrol_designtimeppi_get
,Forms_tcustomdesigncontrol_pixelsperinch_set
,Forms_tcustomdesigncontrol_pixelsperinch_get
,Forms_tcustomdesigncontrol_scaled_set
,Forms_tcustomdesigncontrol_scaled_get
,Forms_tscrollingwincontrol_autoscroll_set
,Forms_tscrollingwincontrol_autoscroll_get
,Forms_tscrollingwincontrol_create
,Forms_tscrollingwincontrol_horzscrollbar_set
,Forms_tscrollingwincontrol_horzscrollbar_get
,Forms_tscrollingwincontrol_vertscrollbar_set
,Forms_tscrollingwincontrol_vertscrollbar_get
;
end.
