import sys
import os
from ctypes import *
from struct import *
if not os.path.isfile('./MIDIData.dll'):
	sys.exit(1)
MIDIData = windll.LoadLibrary('./MIDIData.dll')

MIDIDATA_FORMAT0 = 0x00 # フォーマット0
MIDIDATA_FORMAT1 = 0x01 # フォーマット1
MIDIDATA_FORMAT2 = 0x02 # フォーマット2

MIDIEVENT_SEQUENCENUMBER = 0x00 # シーケンスナンバー(2バイト)
MIDIEVENT_TEXTEVENT = 0x01 # テキスト(可変長文字列)
MIDIEVENT_COPYRIGHTNOTICE = 0x02 # 著作権(可変長文字列)
MIDIEVENT_TRACKNAME = 0x03 # トラック名・シーケンサ名(可変長文字列)
MIDIEVENT_INSTRUMENTNAME = 0x04 # インストゥルメント(可変長文字列)
MIDIEVENT_LYRIC = 0x05 # 歌詞(可変長文字列)
MIDIEVENT_MARKER = 0x06 # マーカー(可変長文字列)
MIDIEVENT_CUEPOINT = 0x07 # キューポイント(可変長文字列)
MIDIEVENT_PROGRAMNAME = 0x08 # プログラム名(可変長文字列)
MIDIEVENT_DEVICENAME = 0x09 # デバイス名(可変長文字列)
MIDIEVENT_CHANNELPREFIX = 0x20 # チャンネルプレフィックス(1バイト)
MIDIEVENT_PORTPREFIX = 0x21 # ポートプレフィックス(1バイト)
MIDIEVENT_ENDOFTRACK = 0x2F # エンドオブトラック(0バイト)
MIDIEVENT_TEMPO = 0x51 # テンポ(3バイト)
MIDIEVENT_SMPTEOFFSET = 0x54 # SMPTEオフセット(5バイト)
MIDIEVENT_TIMESIGNATURE = 0x58 # 拍子記号(4バイト)
MIDIEVENT_KEYSIGNATURE = 0x59 # 調性記号(2バイト)
MIDIEVENT_SEQUENCERSPECIFIC = 0x7F # シーケンサー独自のイベント(可変長バイナリ)
MIDIEVENT_NOTEOFF = 0x80 # ノートオフ(3バイト)
MIDIEVENT_NOTEON = 0x90 # ノートオン(3バイト)
MIDIEVENT_KEYAFTERTOUCH = 0xA0 # キーアフター(3バイト)
MIDIEVENT_CONTROLCHANGE = 0xB0 # コントローラー(3バイト)
MIDIEVENT_PROGRAMCHANGE = 0xC0 # プログラムチェンジ(2バイト)
MIDIEVENT_CHANNELAFTERTOUCH = 0xD0 # チャンネルアフター(2バイト)
MIDIEVENT_PITCHBEND = 0xE0 # ピッチベンド(3バイト)
MIDIEVENT_SYSEXSTART = 0xF0 # システムエクスクルーシヴ(可変長バイナリ)
MIDIEVENT_SYSEXCONTINUE = 0xF7 # システムエクスクルーシヴの続き(可変長バイナリ)

MIDIEVENT_NOTEONNOTEOFF = 0x180 # ノート(0x9n+0x8n)
MIDIEVENT_NOTEONNOTEON0 = 0x190 # ノート(0x9n+0x9n(vel==0))
MIDIEVENT_PATCHCHANGE = 0x1C0 # パッチチェンジ(CC#32+CC#0+プログラムチェンジ)
MIDIEVENT_RPNCHANGE = 0x1A0 # RPNチェンジ(CC#101+CC#100+CC#6)
MIDIEVENT_NRPNCHANGE = 0x1B0 # NRPNチェンジ(CC#99+CC#98+CC#6)

#　MIDIDataクラス関数
# MIDIデータの指定トラックの直前にトラックを挿入
MIDIData_InsertTrackBefore = MIDIData.MIDIData_InsertTrackBefore
MIDIData_InsertTrackBefore.restype = c_bool
MIDIData_InsertTrackBefore.argtypes = (c_void_p,c_void_p,c_void_p,)
# MIDIデータの指定トラックの直後にトラックを挿入
MIDIData_InsertTrackAfter = MIDIData.MIDIData_InsertTrackAfter
MIDIData_InsertTrackAfter.restype = c_bool
MIDIData_InsertTrackAfter.argtypes = (c_void_p,c_void_p,c_void_p,)
# MIDIデータにトラックを追加(トラックは予め生成しておく)
MIDIData_AddTrack = MIDIData.MIDIData_AddTrack
MIDIData_AddTrack.restype = c_uint
MIDIData_AddTrack.argtypes = (c_void_p,c_void_p,)
# MIDIデータ内のトラックを複製する
#MIDIData_DuplicateTrack = MIDIData.MIDIData_DuplicateTrack
#MIDIData_DuplicateTrack.restype = c_void_p
#MIDIData_DuplicateTrack.argtypes = (c_void_p,)
# MIDIデータからトラックを除去(トラック自体及びトラック内のイベントは削除しない)
MIDIData_RemoveTrack = MIDIData.MIDIData_RemoveTrack
MIDIData_RemoveTrack.restype = c_bool
MIDIData_RemoveTrack.argtypes = (c_void_p,c_void_p,)
# MIDIデータの削除(含まれるトラック及びイベントもすべて削除)
MIDIData_Delete = MIDIData.MIDIData_Delete
MIDIData_Delete.restype = None
MIDIData_Delete.argtypes = (c_void_p,)
# MIDIデータを生成し、MIDIデータへのポインタを返す(失敗時NULL)
MIDIData_Create = MIDIData.MIDIData_Create
MIDIData_Create.restype = c_void_p
MIDIData_Create.argtypes = (c_uint,c_uint,c_uint,c_uint,)
# MIDIデータのフォーマット0/1/2を取得
MIDIData_GetFormat = MIDIData.MIDIData_GetFormat
MIDIData_GetFormat.restype = c_uint
MIDIData_GetFormat.argtypes = (c_void_p,)
# MIDIデータのフォーマット0/1/2を設定(変更時コンバート機能を含む)
MIDIData_SetFormat = MIDIData.MIDIData_SetFormat
MIDIData_SetFormat.restype = c_bool
MIDIData_SetFormat.argtypes = (c_void_p,c_uint,)
# MIDIデータのタイムベース取得
MIDIData_GetTimeBase = MIDIData.MIDIData_GetTimeBase
MIDIData_GetTimeBase.restype = c_uint
MIDIData_GetTimeBase.argtypes = (c_void_p,)
# MIDIデータのタイムベースのタイムモード取得
MIDIData_GetTimeMode = MIDIData.MIDIData_GetTimeMode
MIDIData_GetTimeMode.restype = c_uint
MIDIData_GetTimeMode.argtypes = (c_void_p,)
# MIDIデータのタイムベースのレゾリューション取得
MIDIData_GetTimeResolution = MIDIData.MIDIData_GetTimeResolution
MIDIData_GetTimeResolution.restype = c_uint
MIDIData_GetTimeResolution.argtypes = (c_void_p,)
# MIDIデータのタイムベース設定
MIDIData_SetTimeBase = MIDIData.MIDIData_SetTimeBase
MIDIData_SetTimeBase.restype = c_bool
MIDIData_SetTimeBase.argtypes = (c_void_p,c_uint,c_uint,)
# MIDIデータのトラック数取得
MIDIData_GetNumTrack = MIDIData.MIDIData_GetNumTrack
MIDIData_GetNumTrack.restype = c_uint
MIDIData_GetNumTrack.argtypes = (c_void_p,)
# トラック数をカウントし、各トラックのインデックスと総トラック数を更新し、トラック数を返す。
MIDIData_CountTrack = MIDIData.MIDIData_CountTrack
MIDIData_CountTrack.restype = c_uint
MIDIData_CountTrack.argtypes = (c_void_p,)
# XFであるとき、XFのヴァージョンを取得(XFでなければ0)
#MIDIData_GetXFVersion = MIDIData.MIDIData_GetXFVersion
#MIDIData_GetXFVersion.restype = c_void_p
#MIDIData_GetXFVersion.argtypes = (c_void_p,)
# MIDIデータの最初のトラックへのポインタを取得(なければNULL)
MIDIData_GetFirstTrack = MIDIData.MIDIData_GetFirstTrack
MIDIData_GetFirstTrack.restype = c_void_p
MIDIData_GetFirstTrack.argtypes = (c_void_p,)
# MIDIデータの最後のトラックへのポインタを取得(なければNULL)
MIDIData_GetLastTrack = MIDIData.MIDIData_GetLastTrack
MIDIData_GetLastTrack.restype = c_void_p
MIDIData_GetLastTrack.argtypes = (c_void_p,)
# 指定インデックスのMIDIトラックへのポインタを取得する(なければNULL)
MIDIData_GetTrack = MIDIData.MIDIData_GetTrack
MIDIData_GetTrack.restype = c_void_p
MIDIData_GetTrack.argtypes = (c_void_p,c_uint,)
# MIDIデータの開始時刻[Tick]を取得
MIDIData_GetBeginTime = MIDIData.MIDIData_GetBeginTime
MIDIData_GetBeginTime.restype = c_uint
MIDIData_GetBeginTime.argtypes = (c_void_p,)
# MIDIデータの終了時刻[Tick]を取得
MIDIData_GetEndTime = MIDIData.MIDIData_GetEndTime
MIDIData_GetEndTime.restype = c_uint
MIDIData_GetEndTime.argtypes = (c_void_p,)
# MIDIデータのタイトルを簡易取得
#MIDIData_GetTitle = MIDIData.MIDIData_GetTitleW
#MIDIData_GetTitle.restype = c_void_p
#MIDIData_GetTitle.argtypes = (c_void_p,)
# MIDIデータのタイトルを簡易設定
#MIDIData_SetTitle = MIDIData.MIDIData_SetTitleW
#MIDIData_SetTitle.restype = c_void_p
#MIDIData_SetTitle.argtypes = (c_void_p,)
# MIDIデータのサブタイトルを簡易取得
#MIDIData_GetSubTitle = MIDIData.MIDIData_GetSubTitleW
#MIDIData_GetSubTitle.restype = c_void_p
#MIDIData_GetSubTitle.argtypes = (c_void_p,)
# MIDIデータのサブタイトルを簡易設定
#MIDIData_SetSubTitle = MIDIData.MIDIData_SetSubTitleW
#MIDIData_SetSubTitle.restype = c_void_p
#MIDIData_SetSubTitle.argtypes = (c_void_p,)
# MIDIデータの著作権を簡易取得
#MIDIData_GetCopyright = MIDIData.MIDIData_GetCopyrightW
#MIDIData_GetCopyright.restype = c_void_p
#MIDIData_GetCopyright.argtypes = (c_void_p,)
# MIDIデータの著作権を簡易設定
#MIDIData_SetCopyright = MIDIData.MIDIData_SetCopyrightW
#MIDIData_SetCopyright.restype = c_void_p
#MIDIData_SetCopyright.argtypes = (c_void_p,)
# MIDIデータのコメントを簡易取得
#MIDIData_GetComment = MIDIData.MIDIData_GetCommentW
#MIDIData_GetComment.restype = c_void_p
#MIDIData_GetComment.argtypes = (c_void_p,)
# MIDIデータのコメントを簡易設定
#MIDIData_SetComment = MIDIData.MIDIData_SetCommentW
#MIDIData_SetComment.restype = c_void_p
#MIDIData_SetComment.argtypes = (c_void_p,)
# タイムコードをミリ秒に変換(フォーマット0/1の場合のみ)
MIDIData_TimeToMillisec = MIDIData.MIDIData_TimeToMillisec
MIDIData_TimeToMillisec.restype = c_uint
MIDIData_TimeToMillisec.argtypes = (c_void_p,c_uint,)
# ミリ秒をタイムコードに変換(フォーマット0/1の場合のみ)
MIDIData_MillisecToTime = MIDIData.MIDIData_MillisecToTime
MIDIData_MillisecToTime.restype = c_uint
MIDIData_MillisecToTime.argtypes = (c_void_p,c_uint,)
# タイムコードを小節：拍：ティックに分解(最初のトラック内の拍子記号から計算)
#MIDIData_BreakTime = MIDIData.MIDIData_BreakTime
#MIDIData_BreakTime.restype = c_void_p
#MIDIData_BreakTime.argtypes = (c_void_p,)
# タイムコードを小節：拍：ティックに分解(最初のトラック内の拍子記号を基に計算)
#MIDIData_BreakTimeEx = MIDIData.MIDIData_BreakTimeEx
#MIDIData_BreakTimeEx.restype = c_void_p
#MIDIData_BreakTimeEx.argtypes = (c_void_p,)
# 小節：拍：ティックからタイムコードを生成(最初のトラック内の拍子記号から計算)
#MIDIData_MakeTime = MIDIData.MIDIData_MakeTime
#MIDIData_MakeTime.restype = c_void_p
#MIDIData_MakeTime.argtypes = (c_void_p,)
# 小節：拍：ティックからタイムコードを生成(最初のトラック内の拍子記号を基に計算)
#MIDIData_MakeTimeEx = MIDIData.MIDIData_MakeTimeEx
#MIDIData_MakeTimeEx.restype = c_void_p
#MIDIData_MakeTimeEx.argtypes = (c_void_p,)
# 指定位置におけるテンポを取得
#MIDIData_FindTempo = MIDIData.MIDIData_FindTempo
#MIDIData_FindTempo.restype = c_void_p
#MIDIData_FindTempo.argtypes = (c_void_p,)
# 指定位置における拍子記号を取得
#MIDIData_FindTimeSignature = MIDIData.MIDIData_FindTimeSignature
#MIDIData_FindTimeSignature.restype = c_void_p
#MIDIData_FindTimeSignature.argtypes = (c_void_p,)
# 指定位置における調性記号を取得
#MIDIData_FindKeySignature = MIDIData.MIDIData_FindKeySignature
#MIDIData_FindKeySignature.restype = c_void_p
#MIDIData_FindKeySignature.argtypes = (c_void_p,)
# MIDIDataをスタンダードMIDIファイル(SMF)から読み込み、*/
# 新しいMIDIデータへのポインタを返す(失敗時NULL)
MIDIData_LoadFromSMF = MIDIData.MIDIData_LoadFromSMFW
MIDIData_LoadFromSMF.restype = c_void_p
MIDIData_LoadFromSMF.argtypes = (c_wchar_p,)
# MIDIデータをスタンダードMIDIファイル(SMF)として保存
MIDIData_SaveAsSMF = MIDIData.MIDIData_SaveAsSMFW
MIDIData_SaveAsSMF.restype = c_bool
MIDIData_SaveAsSMF.argtypes = (c_void_p,c_wchar_p,)
# MIDIDataをテキストファイルから読み込み、
# 新しいMIDIデータへのポインタを返す(失敗時NULL)
MIDIData_LoadFromText = MIDIData.MIDIData_LoadFromTextW
MIDIData_LoadFromText.restype = c_void_p
MIDIData_LoadFromText.argtypes = (c_wchar_p,)
# MIDIDataをテキストファイルとして保存
MIDIData_SaveAsText = MIDIData.MIDIData_SaveAsTextW
MIDIData_SaveAsText.restype = c_bool
MIDIData_SaveAsText.argtypes = (c_void_p,c_wchar_p,)
# MIDIDataをバイナリファイルから読み込み、*/
# 新しいMIDIデータへのポインタを返す(失敗時NULL)
MIDIData_LoadFromBinary = MIDIData.MIDIData_LoadFromBinaryW
MIDIData_LoadFromBinary.restype = c_void_p
MIDIData_LoadFromBinary.argtypes = (c_wchar_p,)
# MIDIDataをバイナリファイルに保存
MIDIData_SaveAsBinary = MIDIData.MIDIData_SaveAsBinaryW
MIDIData_SaveAsBinary.restype = c_bool
MIDIData_SaveAsBinary.argtypes = (c_void_p,c_wchar_p,)
# MIDIDataをCherrryファイル(*.chy)から読み込み、
# 新しいMIDIデータへのポインタを返す(失敗時NULL)
MIDIData_LoadFromCherry = MIDIData.MIDIData_LoadFromCherryW
MIDIData_LoadFromCherry.restype = c_void_p
MIDIData_LoadFromCherry.argtypes = (c_wchar_p,)
# MIDIデータをCherryファイル(*.chy)に保存
MIDIData_SaveAsCherry = MIDIData.MIDIData_SaveAsCherryW
MIDIData_SaveAsCherry.restype = c_bool
MIDIData_SaveAsCherry.argtypes = (c_void_p,c_wchar_p,)
# MIDIデータをMIDICSVファイル(*.csv)から読み込み
# 新しいMIDIデータへのポインタを返す(失敗時NULL)
MIDIData_LoadFromMIDICSV = MIDIData.MIDIData_LoadFromMIDICSVW
MIDIData_LoadFromMIDICSV.restype = c_void_p
MIDIData_LoadFromMIDICSV.argtypes = (c_wchar_p,)
# MIDIデータをMIDICSVファイル(*.csv)として保存
MIDIData_SaveAsMIDICSV = MIDIData.MIDIData_SaveAsMIDICSVW
MIDIData_SaveAsMIDICSV.restype = c_bool
MIDIData_SaveAsMIDICSV.argtypes = (c_void_p,c_wchar_p,)
# MIDIデータを旧Cakewalkシーケンスファイル(*.wrk)から読み込み
# 新しいMIDIデータへのポインタを返す(失敗時NULL)
MIDIData_LoadFromWRK = MIDIData.MIDIData_LoadFromWRKW
MIDIData_LoadFromWRK.restype = c_void_p
MIDIData_LoadFromWRK.argtypes = (c_wchar_p,)
# MIDIデータをマビノギMMLファイル(*.mml)から読み込み
# 新しいMIDIデータへのポインタを返す(失敗時NULL)
MIDIData_LoadFromMabiMML = MIDIData.MIDIData_LoadFromMabiMMLW
MIDIData_LoadFromMabiMML.restype = c_void_p
MIDIData_LoadFromMabiMML.argtypes = (c_wchar_p,)

#　MIDITrackクラス関数
# トラック内のイベントの総数を取得
#MIDITrack_GetNumEvent = MIDIData.MIDITrack_GetNumEvent
#MIDITrack_GetNumEvent.restype = c_void_p
#MIDITrack_GetNumEvent.argtypes = (c_void_p,)
# トラックの最初のイベントへのポインタを取得(なければNULL)
MIDITrack_GetFirstEvent = MIDIData.MIDITrack_GetFirstEvent
MIDITrack_GetFirstEvent.restype = c_void_p
MIDITrack_GetFirstEvent.argtypes = (c_void_p,)
# トラックの最後のイベントへのポインタを取得(なければNULL)
MIDITrack_GetLastEvent = MIDIData.MIDITrack_GetLastEvent
MIDITrack_GetLastEvent.restype = c_void_p
MIDITrack_GetLastEvent.argtypes = (c_void_p,)
# トラック内の指定種類の最初のイベント取得(なければNULL)
MIDITrack_GetFirstKindEvent = MIDIData.MIDITrack_GetFirstKindEvent
MIDITrack_GetFirstKindEvent.restype = c_void_p
MIDITrack_GetFirstKindEvent.argtypes = (c_void_p,c_uint,)
# トラック内の指定種類の最後のイベント取得(なければNULL)
MIDITrack_GetLastKindEvent = MIDIData.MIDITrack_GetLastKindEvent
MIDITrack_GetLastKindEvent.restype = c_void_p
MIDITrack_GetLastKindEvent.argtypes = (c_void_p,c_uint,)
# 次のMIDIトラックへのポインタ取得(なければNULL)(20080715追加)
MIDITrack_GetNextTrack = MIDIData.MIDITrack_GetNextTrack
MIDITrack_GetNextTrack.restype = c_void_p
MIDITrack_GetNextTrack.argtypes = (c_void_p,)
# 前のMIDIトラックへのポインタ取得(なければNULL)(20080715追加)
MIDITrack_GetPrevTrack = MIDIData.MIDITrack_GetPrevTrack
MIDITrack_GetPrevTrack.restype = c_void_p
MIDITrack_GetPrevTrack.argtypes = (c_void_p,)
# トラックの親MIDIデータへのポインタを取得(なければNULL)
MIDITrack_GetParent = MIDIData.MIDITrack_GetParent
MIDITrack_GetParent.restype = c_void_p
MIDITrack_GetParent.argtypes = (c_void_p,)
# トラック内のイベント数をカウントし、各イベントのインデックスと総イベント数を更新し、イベント数を返す。
MIDITrack_CountEvent = MIDIData.MIDITrack_CountEvent
MIDITrack_CountEvent.restype = c_uint
MIDITrack_CountEvent.argtypes = (c_void_p,)
# トラックの開始時刻(最初のイベントの時刻)[Tick]を取得(20081101追加)
MIDITrack_GetBeginTime = MIDIData.MIDITrack_GetBeginTime
MIDITrack_GetBeginTime.restype = c_uint
MIDITrack_GetBeginTime.argtypes = (c_void_p,)
# トラックの終了時刻(最後のイベントの時刻)[Tick]を取得(20081101追加)
MIDITrack_GetEndTime = MIDIData.MIDITrack_GetEndTime
MIDITrack_GetEndTime.restype = c_uint
MIDITrack_GetEndTime.argtypes = (c_void_p,)
# トラックの名前を簡易に取得
#MIDITrack_GetName = MIDIData.MIDITrack_GetNameW
#MIDITrack_GetName.restype = c_void_p
#MIDITrack_GetName.argtypes = (c_void_p,)
# 入力取得(0=OFF, 1=On)
#MIDITrack_GetInputOn = MIDIData.MIDITrack_GetInputOn
#MIDITrack_GetInputOn.restype = c_void_p
#MIDITrack_GetInputOn.argtypes = (c_void_p,)
# 入力ポート取得(-1=n/a, 0～15=ポート番号)
#MIDITrack_GetInputPort = MIDIData.MIDITrack_GetInputPort
#MIDITrack_GetInputPort.restype = c_void_p
#MIDITrack_GetInputPort.argtypes = (c_void_p,)
# 入力チャンネル取得(-1=n/a, 0～15=チャンネル番号)
#MIDITrack_GetInputChannel = MIDIData.MIDITrack_GetInputChannel
#MIDITrack_GetInputChannel.restype = c_void_p
#MIDITrack_GetInputChannel.argtypes = (c_void_p,)
# 出力取得(0=OFF, 1=On)
#MIDITrack_GetOutputOn = MIDIData.MIDITrack_GetOutputOn
#MIDITrack_GetOutputOn.restype = c_void_p
#MIDITrack_GetOutputOn.argtypes = (c_void_p,)
# 出力ポート(-1=n/a, 0～15=ポート番号)
#MIDITrack_GetOutputPort = MIDIData.MIDITrack_GetOutputPort
#MIDITrack_GetOutputPort.restype = c_void_p
#MIDITrack_GetOutputPort.argtypes = (c_void_p,)
# 出力チャンネル(-1=n/a, 0～15=チャンネル番号)
MIDITrack_GetOutputChannel = MIDIData.MIDITrack_GetOutputChannel
MIDITrack_GetOutputChannel.restype = c_uint
MIDITrack_GetOutputChannel.argtypes = (c_void_p,)
# タイム+取得
#MIDITrack_GetTimePlus = MIDIData.MIDITrack_GetTimePlus
#MIDITrack_GetTimePlus.restype = c_void_p
#MIDITrack_GetTimePlus.argtypes = (c_void_p,)
# キー+取得
#MIDITrack_GetKeyPlus = MIDIData.MIDITrack_GetKeyPlus
#MIDITrack_GetKeyPlus.restype = c_void_p
#MIDITrack_GetKeyPlus.argtypes = (c_void_p,)
# ベロシティ+取得
#MIDITrack_GetVelocityPlus = MIDIData.MIDITrack_GetVelocityPlus
#MIDITrack_GetVelocityPlus.restype = c_void_p
#MIDITrack_GetVelocityPlus.argtypes = (c_void_p,)
# 表示モード取得(0=通常、1=ドラム)
#MIDITrack_GetViewMode = MIDIData.MIDITrack_GetViewMode
#MIDITrack_GetViewMode.restype = c_void_p
#MIDITrack_GetViewMode.argtypes = (c_void_p,)
# 前景色取得
#MIDITrack_GetForeColor = MIDIData.MIDITrack_GetForeColor
#MIDITrack_GetForeColor.restype = c_void_p
#MIDITrack_GetForeColor.argtypes = (c_void_p,)
# 背景色取得
#MIDITrack_GetBackColor = MIDIData.MIDITrack_GetBackColor
#MIDITrack_GetBackColor.restype = c_void_p
#MIDITrack_GetBackColor.argtypes = (c_void_p,)
# トラックの名前を簡易に設定
#MIDITrack_SetName = MIDIData.MIDITrack_SetNameW
#MIDITrack_SetName.restype = c_void_p
#MIDITrack_SetName.argtypes = (c_void_p,)
# 入力設定(0=OFF, 1=On)
#MIDITrack_SetInputOn = MIDIData.MIDITrack_SetInputOn
#MIDITrack_SetInputOn.restype = c_void_p
#MIDITrack_SetInputOn.argtypes = (c_void_p,)
# 入力ポート設定(-1=n/a, 0～15=ポート番号)
#MIDITrack_SetInputPort = MIDIData.MIDITrack_SetInputPort
#MIDITrack_SetInputPort.restype = c_void_p
#MIDITrack_SetInputPort.argtypes = (c_void_p,)
# 入力チャンネル設定(-1=n/a, 0～15=チャンネル番号)
#MIDITrack_SetInputChannel = MIDIData.MIDITrack_SetInputChannel
#MIDITrack_SetInputChannel.restype = c_void_p
#MIDITrack_SetInputChannel.argtypes = (c_void_p,)
# 出力設定(0=OFF, 1=On)
#MIDITrack_SetOutputOn = MIDIData.MIDITrack_SetOutputOn
#MIDITrack_SetOutputOn.restype = c_void_p
#MIDITrack_SetOutputOn.argtypes = (c_void_p,)
# 出力ポート(-1=n/a, 0～15=ポート番号)
#MIDITrack_SetOutputPort = MIDIData.MIDITrack_SetOutputPort
#MIDITrack_SetOutputPort.restype = c_void_p
#MIDITrack_SetOutputPort.argtypes = (c_void_p,)
# 出力チャンネル(-1=n/a, 0～15=チャンネル番号)
MIDITrack_SetOutputChannel = MIDIData.MIDITrack_SetOutputChannel
MIDITrack_SetOutputChannel.restype = c_bool
MIDITrack_SetOutputChannel.argtypes = (c_void_p,c_uint,)
# タイム+設定
#MIDITrack_SetTimePlus = MIDIData.MIDITrack_SetTimePlus
#MIDITrack_SetTimePlus.restype = c_void_p
#MIDITrack_SetTimePlus.argtypes = (c_void_p,)
# キー+設定
#MIDITrack_SetKeyPlus = MIDIData.MIDITrack_SetKeyPlus
#MIDITrack_SetKeyPlus.restype = c_void_p
#MIDITrack_SetKeyPlus.argtypes = (c_void_p,)
# ベロシティ+設定
#MIDITrack_SetVelocityPlus = MIDIData.MIDITrack_SetVelocityPlus
#MIDITrack_SetVelocityPlus.restype = c_void_p
#MIDITrack_SetVelocityPlus.argtypes = (c_void_p,)
# 表示モード設定(0=通常、1=ドラム)
#MIDITrack_SetViewMode = MIDIData.MIDITrack_SetViewMode
#MIDITrack_SetViewMode.restype = c_void_p
#MIDITrack_SetViewMode.argtypes = (c_void_p,)
# 前景色設定
#MIDITrack_SetForeColor = MIDIData.MIDITrack_SetForeColor
#MIDITrack_SetForeColor.restype = c_void_p
#MIDITrack_SetForeColor.argtypes = (c_void_p,)
# 背景色設定
#MIDITrack_SetBackColor = MIDIData.MIDITrack_SetBackColor
#MIDITrack_SetBackColor.restype = c_void_p
#MIDITrack_SetBackColor.argtypes = (c_void_p,)
# XFであるとき、XFのヴァージョンを取得(XFでなければ0)
#MIDITrack_GetXFVersion = MIDIData.MIDITrack_GetXFVersion
#MIDITrack_GetXFVersion.restype = c_void_p
#MIDITrack_GetXFVersion.argtypes = (c_void_p,)
# トラックの削除(含まれるイベントオブジェクトも削除されます)
MIDITrack_Delete = MIDIData.MIDITrack_Delete
MIDITrack_Delete.restype = None
MIDITrack_Delete.argtypes = (c_void_p,)
# トラックを生成し、トラックへのポインタを返す(失敗時NULL)
MIDITrack_Create = MIDIData.MIDITrack_Create
MIDITrack_Create.restype = c_void_p
MIDITrack_Create.argtypes = ()
# MIDIトラックのクローンを生成
MIDITrack_CreateClone = MIDIData.MIDITrack_CreateClone
MIDITrack_CreateClone.restype = c_void_p
MIDITrack_CreateClone.argtypes = (c_void_p,)
# トラックにイベントを挿入(イベントはあらかじめ生成しておく)
#MIDITrack_InsertSingleEventAfter = MIDIData.MIDITrack_InsertSingleEventAfter
#MIDITrack_InsertSingleEventAfter.restype = c_void_p
#MIDITrack_InsertSingleEventAfter.argtypes = (c_void_p,)
# トラックにイベントを挿入(イベントはあらかじめ生成しておく)
#MIDITrack_InsertSingleEventBefore = MIDIData.MIDITrack_InsertSingleEventBefore
#MIDITrack_InsertSingleEventBefore.restype = c_void_p
#MIDITrack_InsertSingleEventBefore.argtypes = (c_void_p,)
# トラックにイベントを挿入(イベントはあらかじめ生成しておく)
MIDITrack_InsertEventAfter = MIDIData.MIDITrack_InsertEventAfter
MIDITrack_InsertEventAfter.restype = c_uint
MIDITrack_InsertEventAfter.argtypes = (c_void_p,c_void_p,c_void_p,)
# トラックにイベントを挿入(イベントはあらかじめ生成しておく)
MIDITrack_InsertEventBefore = MIDIData.MIDITrack_InsertEventBefore
MIDITrack_InsertEventBefore.restype = c_uint
MIDITrack_InsertEventBefore.argtypes = (c_void_p,c_void_p,c_void_p,)
# トラックにイベントを挿入(イベントはあらかじめ生成しておく)
MIDITrack_InsertEvent = MIDIData.MIDITrack_InsertEvent
MIDITrack_InsertEvent.restype = c_uint
MIDITrack_InsertEvent.argtypes = (c_void_p,c_void_p,)
# トラックにシーケンス番号イベントを生成して挿入
#MIDITrack_InsertSequenceNumber = MIDIData.MIDITrack_InsertSequenceNumber
#MIDITrack_InsertSequenceNumber.restype = c_void_p
#MIDITrack_InsertSequenceNumber.argtypes = (c_void_p,)
# トラックにテキストベースのイベントを生成して挿入
#MIDITrack_InsertTextBasedEvent = MIDIData.MIDITrack_InsertTextBasedEventW
#MIDITrack_InsertTextBasedEvent.restype = c_void_p
#MIDITrack_InsertTextBasedEvent.argtypes = (c_void_p,)
# トラックにテキストベースのイベントを生成して挿入(文字コード指定あり)
#MIDITrack_InsertTextBasedEventEx = MIDIData.MIDITrack_InsertTextBasedEventExW
#MIDITrack_InsertTextBasedEventEx.restype = c_void_p
#MIDITrack_InsertTextBasedEventEx.argtypes = (c_void_p,)
# トラックにテキストイベントを生成して挿入
#MIDITrack_InsertTextEvent = MIDIData.MIDITrack_InsertTextEventW
#MIDITrack_InsertTextEvent.restype = c_void_p
#MIDITrack_InsertTextEvent.argtypes = (c_void_p,)
# トラックにテキストイベントを生成して挿入(文字コード指定あり)
#MIDITrack_InsertTextEventEx = MIDIData.MIDITrack_InsertTextEventExW
#MIDITrack_InsertTextEventEx.restype = c_void_p
#MIDITrack_InsertTextEventEx.argtypes = (c_void_p,)
# トラックに著作権イベントを生成して挿入
#MIDITrack_InsertCopyrightNotice = MIDIData.MIDITrack_InsertCopyrightNoticeW
#MIDITrack_InsertCopyrightNotice.restype = c_void_p
#MIDITrack_InsertCopyrightNotice.argtypes = (c_void_p,)
# トラックに著作権イベントを生成して挿入(文字コード指定あり)
#MIDITrack_InsertCopyrightNoticeEx = MIDIData.MIDITrack_InsertCopyrightNoticeExW
#MIDITrack_InsertCopyrightNoticeEx.restype = c_void_p
#MIDITrack_InsertCopyrightNoticeEx.argtypes = (c_void_p,)
# トラックにトラック名イベントを生成して挿入
#MIDITrack_InsertTrackName = MIDIData.MIDITrack_InsertTrackNameW
#MIDITrack_InsertTrackName.restype = c_void_p
#MIDITrack_InsertTrackName.argtypes = (c_void_p,)
# トラックにトラック名イベントを生成して挿入(文字コード指定あり)
#MIDITrack_InsertTrackNameEx = MIDIData.MIDITrack_InsertTrackNameExW
#MIDITrack_InsertTrackNameEx.restype = c_void_p
#MIDITrack_InsertTrackNameEx.argtypes = (c_void_p,)
# トラックにインストゥルメント名イベントを生成して挿入
#MIDITrack_InsertInstrumentName = MIDIData.MIDITrack_InsertInstrumentNameW
#MIDITrack_InsertInstrumentName.restype = c_void_p
#MIDITrack_InsertInstrumentName.argtypes = (c_void_p,)
# トラックにインストゥルメント名イベントを生成して挿入(文字コード指定あり)
#MIDITrack_InsertInstrumentNameEx = MIDIData.MIDITrack_InsertInstrumentNameExW
#MIDITrack_InsertInstrumentNameEx.restype = c_void_p
#MIDITrack_InsertInstrumentNameEx.argtypes = (c_void_p,)
# トラックに歌詞イベントを生成して挿入
#MIDITrack_InsertLyric = MIDIData.MIDITrack_InsertLyricW
#MIDITrack_InsertLyric.restype = c_void_p
#MIDITrack_InsertLyric.argtypes = (c_void_p,)
# トラックに歌詞イベントを生成して挿入(文字コード指定あり)
#MIDITrack_InsertLyricEx = MIDIData.MIDITrack_InsertLyricExW
#MIDITrack_InsertLyricEx.restype = c_void_p
#MIDITrack_InsertLyricEx.argtypes = (c_void_p,)
# トラックにマーカーイベントを生成して挿入
MIDITrack_InsertMarker = MIDIData.MIDITrack_InsertMarkerW
MIDITrack_InsertMarker.restype = c_bool
MIDITrack_InsertMarker.argtypes = (c_void_p,c_uint,c_wchar_p,)
# トラックにマーカーイベントを生成して挿入(文字コード指定あり)
#MIDITrack_InsertMarkerEx = MIDIData.MIDITrack_InsertMarkerExW
#MIDITrack_InsertMarkerEx.restype = c_void_p
#MIDITrack_InsertMarkerEx.argtypes = (c_void_p,)
# トラックにキューポイントイベントを生成して挿入
#MIDITrack_InsertCuePoint = MIDIData.MIDITrack_InsertCuePointW
#MIDITrack_InsertCuePoint.restype = c_void_p
#MIDITrack_InsertCuePoint.argtypes = (c_void_p,)
# トラックにキューポイントイベントを生成して挿入(文字コード指定あり)
#MIDITrack_InsertCuePointEx = MIDIData.MIDITrack_InsertCuePointExW
#MIDITrack_InsertCuePointEx.restype = c_void_p
#MIDITrack_InsertCuePointEx.argtypes = (c_void_p,)
# トラックにプログラム名イベントを生成して挿入
#MIDITrack_InsertProgramName = MIDIData.MIDITrack_InsertProgramNameW
#MIDITrack_InsertProgramName.restype = c_void_p
#MIDITrack_InsertProgramName.argtypes = (c_void_p,)
# トラックにプログラム名イベントを生成して挿入(文字コード指定あり)
#MIDITrack_InsertProgramNameEx = MIDIData.MIDITrack_InsertProgramNameExW
#MIDITrack_InsertProgramNameEx.restype = c_void_p
#MIDITrack_InsertProgramNameEx.argtypes = (c_void_p,)
# トラックにデバイス名イベントを生成して挿入
#MIDITrack_InsertDeviceName = MIDIData.MIDITrack_InsertDeviceNameW
#MIDITrack_InsertDeviceName.restype = c_void_p
#MIDITrack_InsertDeviceName.argtypes = (c_void_p,)
# トラックにデバイス名イベントを生成して挿入(文字コード指定あり)
#MIDITrack_InsertDeviceNameEx = MIDIData.MIDITrack_InsertDeviceNameExW
#MIDITrack_InsertDeviceNameEx.restype = c_void_p
#MIDITrack_InsertDeviceNameEx.argtypes = (c_void_p,)
# トラックにチャンネルプレフィックスイベントを生成して挿入
#MIDITrack_InsertChannelPrefix = MIDIData.MIDITrack_InsertChannelPrefix
#MIDITrack_InsertChannelPrefix.restype = c_void_p
#MIDITrack_InsertChannelPrefix.argtypes = (c_void_p,)
# トラックにポートプレフィックスイベントを生成して挿入
#MIDITrack_InsertPortPrefix = MIDIData.MIDITrack_InsertPortPrefix
#MIDITrack_InsertPortPrefix.restype = c_void_p
#MIDITrack_InsertPortPrefix.argtypes = (c_void_p,)
# トラックにエンドオブトラックイベントを生成して挿入
MIDITrack_InsertEndofTrack = MIDIData.MIDITrack_InsertEndofTrack
MIDITrack_InsertEndofTrack.restype = c_bool
MIDITrack_InsertEndofTrack.argtypes = (c_void_p,c_uint,)
# トラックにテンポイベントを生成して挿入
MIDITrack_InsertTempo = MIDIData.MIDITrack_InsertTempo
MIDITrack_InsertTempo.restype = c_bool
MIDITrack_InsertTempo.argtypes = (c_void_p,c_uint,c_uint,)
# トラックにSMPTEオフセットイベントを生成して挿入
#MIDITrack_InsertSMPTEOffset = MIDIData.MIDITrack_InsertSMPTEOffset
#MIDITrack_InsertSMPTEOffset.restype = c_void_p
#MIDITrack_InsertSMPTEOffset.argtypes = (c_void_p,)
# トラックに拍子記号イベントを生成して挿入
#MIDITrack_InsertTimeSignature = MIDIData.MIDITrack_InsertTimeSignature
#MIDITrack_InsertTimeSignature.restype = c_void_p
#MIDITrack_InsertTimeSignature.argtypes = (c_void_p,)
# トラックに調性記号イベントを生成して挿入
#MIDITrack_InsertKeySignature = MIDIData.MIDITrack_InsertKeySignature
#MIDITrack_InsertKeySignature.restype = c_void_p
#MIDITrack_InsertKeySignature.argtypes = (c_void_p,)
# トラックにシーケンサー独自のイベントを生成して挿入
#MIDITrack_InsertSequencerSpecific = MIDIData.MIDITrack_InsertSequencerSpecific
#MIDITrack_InsertSequencerSpecific.restype = c_void_p
#MIDITrack_InsertSequencerSpecific.argtypes = (c_void_p,)
# トラックにノートオフイベントを生成して挿入
#MIDITrack_InsertNoteOff = MIDIData.MIDITrack_InsertNoteOff
#MIDITrack_InsertNoteOff.restype = c_void_p
#MIDITrack_InsertNoteOff.argtypes = (c_void_p,)
# トラックにノートオンイベントを生成して挿入
#MIDITrack_InsertNoteOn = MIDIData.MIDITrack_InsertNoteOn
#MIDITrack_InsertNoteOn.restype = c_void_p
#MIDITrack_InsertNoteOn.argtypes = (c_void_p,)
# トラックにノートイベントを生成して挿入
MIDITrack_InsertNote = MIDIData.MIDITrack_InsertNote
MIDITrack_InsertNote.restype = c_uint
MIDITrack_InsertNote.argtypes = (c_void_p,c_uint,c_uint,c_uint,c_uint,c_uint,)
# トラックにキーアフタータッチイベントを生成して挿入
#MIDITrack_InsertKeyAftertouch = MIDIData.MIDITrack_InsertKeyAftertouch
#MIDITrack_InsertKeyAftertouch.restype = c_void_p
#MIDITrack_InsertKeyAftertouch.argtypes = (c_void_p,)
# トラックにコントロールチェンジイベントを生成して挿入
MIDITrack_InsertControlChange = MIDIData.MIDITrack_InsertControlChange
MIDITrack_InsertControlChange.restype = c_bool
MIDITrack_InsertControlChange.argtypes = (c_void_p,c_uint,c_uint,c_uint,c_uint,)
# トラックにRPNチェンジイベントを生成して挿入
#MIDITrack_InsertRPNChange = MIDIData.MIDITrack_InsertRPNChange
#MIDITrack_InsertRPNChange.restype = c_void_p
#MIDITrack_InsertRPNChange.argtypes = (c_void_p,)
# トラックにNRPNチェンジイベントを生成して挿入
#MIDITrack_InsertNRPNChange = MIDIData.MIDITrack_InsertNRPNChange
#MIDITrack_InsertNRPNChange.restype = c_void_p
#MIDITrack_InsertNRPNChange.argtypes = (c_void_p,)
# トラックにプログラムチェンジイベントを生成して挿入
MIDITrack_InsertProgramChange = MIDIData.MIDITrack_InsertProgramChange
MIDITrack_InsertProgramChange.restype = c_bool
MIDITrack_InsertProgramChange.argtypes = (c_void_p,c_uint,c_uint,c_uint,)
# トラックにパッチチェンジイベントを生成して挿入
#MIDITrack_InsertPatchChange = MIDIData.MIDITrack_InsertPatchChange
#MIDITrack_InsertPatchChange.restype = c_void_p
#MIDITrack_InsertPatchChange.argtypes = (c_void_p,)
# トラックにチャンネルアフターイベントを生成して挿入
#MIDITrack_InsertChannelAftertouch = MIDIData.MIDITrack_InsertChannelAftertouch
#MIDITrack_InsertChannelAftertouch.restype = c_void_p
#MIDITrack_InsertChannelAftertouch.argtypes = (c_void_p,)
# トラックにピッチベンドイベントを生成して挿入
MIDITrack_InsertPitchBend = MIDIData.MIDITrack_InsertPitchBend
MIDITrack_InsertPitchBend.restype = c_bool
MIDITrack_InsertPitchBend.argtypes = (c_void_p,c_uint,c_uint,c_uint,)
# トラックにシステムエクスクルーシヴイベントを生成して挿入
#MIDITrack_InsertSysExEvent = MIDIData.MIDITrack_InsertSysExEvent
#MIDITrack_InsertSysExEvent.restype = c_void_p
#MIDITrack_InsertSysExEvent.argtypes = (c_void_p,)
# トラックからイベントを1つ取り除く(イベントオブジェクトは削除しません)
#MIDITrack_RemoveSingleEvent = MIDIData.MIDITrack_RemoveSingleEvent
#MIDITrack_RemoveSingleEvent.restype = c_void_p
#MIDITrack_RemoveSingleEvent.argtypes = (c_void_p,)
# トラックからイベントを取り除く(イベントオブジェクトは削除しません)
MIDITrack_RemoveEvent = MIDIData.MIDITrack_RemoveEvent
MIDITrack_RemoveEvent.restype = c_uint
MIDITrack_RemoveEvent.argtypes = (c_void_p,c_void_p,)
# MIDIトラックが浮遊トラックであるかどうかを調べる
MIDITrack_IsFloating = MIDIData.MIDITrack_IsFloating
MIDITrack_IsFloating.restype = c_bool
MIDITrack_IsFloating.argtypes = (c_void_p,)
# MIDIトラックがセットアップトラックとして正しいことを確認する
MIDITrack_CheckSetupTrack = MIDIData.MIDITrack_CheckSetupTrack
MIDITrack_CheckSetupTrack.restype = c_bool
MIDITrack_CheckSetupTrack.argtypes = (c_void_p,)
# MIDIトラックがノンセットアップトラックとして正しいことを確認する
MIDITrack_CheckNonSetupTrack = MIDIData.MIDITrack_CheckNonSetupTrack
MIDITrack_CheckNonSetupTrack.restype = c_bool
MIDITrack_CheckNonSetupTrack.argtypes = (c_void_p,)
# タイムコードをミリ秒時刻に変換(指定トラック内のテンポイベントを基に計算)
MIDITrack_TimeToMillisec = MIDIData.MIDITrack_TimeToMillisec
MIDITrack_TimeToMillisec.restype = c_uint
MIDITrack_TimeToMillisec.argtypes = (c_void_p,c_uint,)
# ミリ秒時刻をタイムコードに変換(指定トラック内のテンポイベントを基に計算)
MIDITrack_MillisecToTime = MIDIData.MIDITrack_MillisecToTime
MIDITrack_MillisecToTime.restype = c_uint
MIDITrack_MillisecToTime.argtypes = (c_void_p,c_uint,)
# タイムコードを小節：拍：ティックに分解(指定トラック内の拍子記号を基に計算)
#MIDITrack_BreakTimeEx = MIDIData.MIDITrack_BreakTimeEx
#MIDITrack_BreakTimeEx.restype = c_void_p
#MIDITrack_BreakTimeEx.argtypes = (c_void_p,)
# タイムコードを小節：拍：ティックに分解(指定トラック内の拍子記号を基に計算)
#MIDITrack_BreakTime = MIDIData.MIDITrack_BreakTime
#MIDITrack_BreakTime.restype = c_void_p
#MIDITrack_BreakTime.argtypes = (c_void_p,)
# 小節：拍：ティックからタイムコードを生成(指定トラック内の拍子記号を基に計算)
#MIDITrack_MakeTimeEx = MIDIData.MIDITrack_MakeTimeEx
#MIDITrack_MakeTimeEx.restype = c_void_p
#MIDITrack_MakeTimeEx.argtypes = (c_void_p,)
# 小節：拍：ティックからタイムコードを生成(指定トラック内の拍子記号を基に計算)
#MIDITrack_MakeTime = MIDIData.MIDITrack_MakeTime
#MIDITrack_MakeTime.restype = c_void_p
#MIDITrack_MakeTime.argtypes = (c_void_p,)
# 指定位置におけるテンポを取得
#MIDITrack_FindTempo = MIDIData.MIDITrack_FindTempo
#MIDITrack_FindTempo.restype = c_void_p
#MIDITrack_FindTempo.argtypes = (c_void_p,)
# 指定位置における拍子記号を取得
#MIDITrack_FindTimeSignature = MIDIData.MIDITrack_FindTimeSignature
#MIDITrack_FindTimeSignature.restype = c_void_p
#MIDITrack_FindTimeSignature.argtypes = (c_void_p,)
# 指定位置における調性記号を取得
#MIDITrack_FindKeySignature = MIDIData.MIDITrack_FindKeySignature
#MIDITrack_FindKeySignature.restype = c_void_p
#MIDITrack_FindKeySignature.argtypes = (c_void_p,)

#　MIDIEventクラス関数
# 結合イベントの最初のイベントを返す。 */
# 結合イベントでない場合、pEvent自身を返す。*/
#MIDIEvent_GetFirstCombinedEvent = MIDIData.MIDIEvent_GetFirstCombinedEvent
#MIDIEvent_GetFirstCombinedEvent.restype = c_void_p
#MIDIEvent_GetFirstCombinedEvent.argtypes = (c_void_p,)
# 結合イベントの最後のイベントを返す。 */
# 結合イベントでない場合、pEvent自身を返す。*/
#MIDIEvent_GetLastCombinedEvent = MIDIData.MIDIEvent_GetLastCombinedEvent
#MIDIEvent_GetLastCombinedEvent.restype = c_void_p
#MIDIEvent_GetLastCombinedEvent.argtypes = (c_void_p,)
# 単体イベントを結合する */
MIDIEvent_Combine = MIDIData.MIDIEvent_Combine
MIDIEvent_Combine.restype = c_uint
MIDIEvent_Combine.argtypes = (c_void_p,)
# 結合イベントを切り離す */
#MIDIEvent_Chop = MIDIData.MIDIEvent_Chop
#MIDIEvent_Chop.restype = c_void_p
#MIDIEvent_Chop.argtypes = (c_void_p,)
# MIDIイベントの削除(結合している場合でも単一のMIDIイベントを削除) */
#MIDIEvent_DeleteSingle = MIDIData.MIDIEvent_DeleteSingle
#MIDIEvent_DeleteSingle.restype = c_void_p
#MIDIEvent_DeleteSingle.argtypes = (c_void_p,)
# MIDIイベントの削除(結合している場合、結合しているMIDIイベントも削除) */
MIDIEvent_Delete = MIDIData.MIDIEvent_Delete
MIDIEvent_Delete.restype = c_uint
MIDIEvent_Delete.argtypes = (c_void_p,)
# MIDIイベント(任意)を生成し、MIDIイベントへのポインタを返す(失敗時NULL、以下同様) */
#MIDIEvent_Create = MIDIData.MIDIEvent_Create
#MIDIEvent_Create.restype = c_void_p
#MIDIEvent_Create.argtypes = (c_void_p,)
# 指定イベントと同じMIDIイベントを生成し、MIDIイベントへのポインタを返す(失敗時NULL、以下同様) */
MIDIEvent_CreateClone = MIDIData.MIDIEvent_CreateClone
MIDIEvent_CreateClone.restype = c_void_p
MIDIEvent_CreateClone.argtypes = (c_void_p,)
# シーケンス番号イベントの生成 */
#MIDIEvent_CreateSequenceNumber = MIDIData.MIDIEvent_CreateSequenceNumber
#MIDIEvent_CreateSequenceNumber.restype = c_void_p
#MIDIEvent_CreateSequenceNumber.argtypes = (c_void_p,)
# テキストベースのイベントの生成 */
#MIDIEvent_CreateTextBasedEvent = MIDIData.MIDIEvent_CreateTextBasedEventW
#MIDIEvent_CreateTextBasedEvent.restype = c_void_p
#MIDIEvent_CreateTextBasedEvent.argtypes = (c_void_p,)
# テキストベースのイベントの生成(文字コード指定あり) */
#MIDIEvent_CreateTextBasedEventEx = MIDIData.MIDIEvent_CreateTextBasedEventExW
#MIDIEvent_CreateTextBasedEventEx.restype = c_void_p
#MIDIEvent_CreateTextBasedEventEx.argtypes = (c_void_p,)
# テキストイベントの生成 */
#MIDIEvent_CreateTextEvent = MIDIData.MIDIEvent_CreateTextEventW
#MIDIEvent_CreateTextEvent.restype = c_void_p
#MIDIEvent_CreateTextEvent.argtypes = (c_void_p,)
# テキストイベントの生成(文字コード指定あり) */
#MIDIEvent_CreateTextEventEx = MIDIData.MIDIEvent_CreateTextEventExW
#MIDIEvent_CreateTextEventEx.restype = c_void_p
#MIDIEvent_CreateTextEventEx.argtypes = (c_void_p,)
# 著作権イベントの生成 */
#MIDIEvent_CreateCopyrightNotice = MIDIData.MIDIEvent_CreateCopyrightNoticeW
#MIDIEvent_CreateCopyrightNotice.restype = c_void_p
#MIDIEvent_CreateCopyrightNotice.argtypes = (c_void_p,)
# 著作権イベントの生成(文字コード指定あり) */
#MIDIEvent_CreateCopyrightNoticeEx = MIDIData.MIDIEvent_CreateCopyrightNoticeExW
#MIDIEvent_CreateCopyrightNoticeEx.restype = c_void_p
#MIDIEvent_CreateCopyrightNoticeEx.argtypes = (c_void_p,)
# トラック名イベントの生成 */
#MIDIEvent_CreateTrackName = MIDIData.MIDIEvent_CreateTrackNameW
#MIDIEvent_CreateTrackName.restype = c_void_p
#MIDIEvent_CreateTrackName.argtypes = (c_void_p,)
# トラック名イベントの生成(文字コード指定あり) */
#MIDIEvent_CreateTrackNameEx = MIDIData.MIDIEvent_CreateTrackNameExW
#MIDIEvent_CreateTrackNameEx.restype = c_void_p
#MIDIEvent_CreateTrackNameEx.argtypes = (c_void_p,)
# インストゥルメント名イベントの生成 */
#MIDIEvent_CreateInstrumentName = MIDIData.MIDIEvent_CreateInstrumentNameW
#MIDIEvent_CreateInstrumentName.restype = c_void_p
#MIDIEvent_CreateInstrumentName.argtypes = (c_void_p,)
# インストゥルメント名イベントの生成(文字コード指定あり) */
#MIDIEvent_CreateInstrumentNameEx = MIDIData.MIDIEvent_CreateInstrumentNameExW
#MIDIEvent_CreateInstrumentNameEx.restype = c_void_p
#MIDIEvent_CreateInstrumentNameEx.argtypes = (c_void_p,)
# 歌詞イベントの生成 */
#MIDIEvent_CreateLyric = MIDIData.MIDIEvent_CreateLyricW
#MIDIEvent_CreateLyric.restype = c_void_p
#MIDIEvent_CreateLyric.argtypes = (c_void_p,)
# 歌詞イベントの生成(文字コード指定あり) */
#MIDIEvent_CreateLyricEx = MIDIData.MIDIEvent_CreateLyricExW
#MIDIEvent_CreateLyricEx.restype = c_void_p
#MIDIEvent_CreateLyricEx.argtypes = (c_void_p,)
# マーカーイベントの生成 */
#MIDIEvent_CreateMarker = MIDIData.MIDIEvent_CreateMarkerW
#MIDIEvent_CreateMarker.restype = c_void_p
#MIDIEvent_CreateMarker.argtypes = (c_void_p,)
# マーカーイベントの生成(文字コード指定あり) */
#MIDIEvent_CreateMarkerEx = MIDIData.MIDIEvent_CreateMarkerExW
#MIDIEvent_CreateMarkerEx.restype = c_void_p
#MIDIEvent_CreateMarkerEx.argtypes = (c_void_p,)
# キューポイントイベントの生成 */
#MIDIEvent_CreateCuePoint = MIDIData.MIDIEvent_CreateCuePointW
#MIDIEvent_CreateCuePoint.restype = c_void_p
#MIDIEvent_CreateCuePoint.argtypes = (c_void_p,)
# キューポイントイベントの生成(文字コード指定あり) */
#MIDIEvent_CreateCuePointEx = MIDIData.MIDIEvent_CreateCuePointExW
#MIDIEvent_CreateCuePointEx.restype = c_void_p
#MIDIEvent_CreateCuePointEx.argtypes = (c_void_p,)
# プログラム名イベントの生成 */
#MIDIEvent_CreateProgramName = MIDIData.MIDIEvent_CreateProgramNameW
#MIDIEvent_CreateProgramName.restype = c_void_p
#MIDIEvent_CreateProgramName.argtypes = (c_void_p,)
# プログラム名イベントの生成(文字コード指定あり) */
#MIDIEvent_CreateProgramNameEx = MIDIData.MIDIEvent_CreateProgramNameExW
#MIDIEvent_CreateProgramNameEx.restype = c_void_p
#MIDIEvent_CreateProgramNameEx.argtypes = (c_void_p,)
# デバイス名イベント生成 */
#MIDIEvent_CreateDeviceName = MIDIData.MIDIEvent_CreateDeviceNameW
#MIDIEvent_CreateDeviceName.restype = c_void_p
#MIDIEvent_CreateDeviceName.argtypes = (c_void_p,)
# デバイス名イベント生成(文字コード指定あり) */
#MIDIEvent_CreateDeviceNameEx = MIDIData.MIDIEvent_CreateDeviceNameExW
#MIDIEvent_CreateDeviceNameEx.restype = c_void_p
#MIDIEvent_CreateDeviceNameEx.argtypes = (c_void_p,)
# チャンネルプレフィックスイベントの生成 */
#MIDIEvent_CreateChannelPrefix = MIDIData.MIDIEvent_CreateChannelPrefix
#MIDIEvent_CreateChannelPrefix.restype = c_void_p
#MIDIEvent_CreateChannelPrefix.argtypes = (c_void_p,)
# ポートプレフィックスイベントの生成 */
#MIDIEvent_CreatePortPrefix = MIDIData.MIDIEvent_CreatePortPrefix
#MIDIEvent_CreatePortPrefix.restype = c_void_p
#MIDIEvent_CreatePortPrefix.argtypes = (c_void_p,)
# エンドオブトラックイベントの生成 */
#MIDIEvent_CreateEndofTrack = MIDIData.MIDIEvent_CreateEndofTrack
#MIDIEvent_CreateEndofTrack.restype = c_void_p
#MIDIEvent_CreateEndofTrack.argtypes = (c_void_p,)
# テンポイベントの生成 */
#MIDIEvent_CreateTempo = MIDIData.MIDIEvent_CreateTempo
#MIDIEvent_CreateTempo.restype = c_void_p
#MIDIEvent_CreateTempo.argtypes = (c_void_p,)
# SMPTEオフセットイベントの生成 */
#MIDIEvent_CreateSMPTEOffset = MIDIData.MIDIEvent_CreateSMPTEOffset
#MIDIEvent_CreateSMPTEOffset.restype = c_void_p
#MIDIEvent_CreateSMPTEOffset.argtypes = (c_void_p,)
# 拍子記号イベントの生成 */
#MIDIEvent_CreateTimeSignature = MIDIData.MIDIEvent_CreateTimeSignature
#MIDIEvent_CreateTimeSignature.restype = c_void_p
#MIDIEvent_CreateTimeSignature.argtypes = (c_void_p,)
# 調性記号イベントの生成 */
#MIDIEvent_CreateKeySignature = MIDIData.MIDIEvent_CreateKeySignature
#MIDIEvent_CreateKeySignature.restype = c_void_p
#MIDIEvent_CreateKeySignature.argtypes = (c_void_p,)
# シーケンサー独自のイベントの生成 */
#MIDIEvent_CreateSequencerSpecific = MIDIData.MIDIEvent_CreateSequencerSpecific
#MIDIEvent_CreateSequencerSpecific.restype = c_void_p
#MIDIEvent_CreateSequencerSpecific.argtypes = (c_void_p,)
# ノートオフイベントの生成 */
#MIDIEvent_CreateNoteOff = MIDIData.MIDIEvent_CreateNoteOff
#MIDIEvent_CreateNoteOff.restype = c_void_p
#MIDIEvent_CreateNoteOff.argtypes = (c_void_p,)
# ノートオンイベントの生成 */
#MIDIEvent_CreateNoteOn = MIDIData.MIDIEvent_CreateNoteOn
#MIDIEvent_CreateNoteOn.restype = c_void_p
#MIDIEvent_CreateNoteOn.argtypes = (c_void_p,)
# ノートイベントの生成(MIDIEvent_CreateNoteOnNoteOn0と同じ) */
# (ノートオン・ノートオン(0x9n(vel==0))の2イベントを生成し、*/
# ノートオンイベントへのポインタを返す。) */
#MIDIEvent_CreateNote = MIDIData.MIDIEvent_CreateNote
#MIDIEvent_CreateNote.restype = c_void_p
#MIDIEvent_CreateNote.argtypes = (c_void_p,)
# ノートイベントの生成(0x8n離鍵型) */
# (ノートオン(0x9n)・ノートオフ(0x8n)の2イベントを生成し、*/
# NoteOnへのポインタを返す) */
#MIDIEvent_CreateNoteOnNoteOff = MIDIData.MIDIEvent_CreateNoteOnNoteOff
#MIDIEvent_CreateNoteOnNoteOff.restype = c_void_p
#MIDIEvent_CreateNoteOnNoteOff.argtypes = (c_void_p,)
# ノートイベントの生成(0x9n離鍵型) */
# (ノートオン(0x9n)・ノートオン(0x9n(vel==0))の2イベントを生成し、*/
# NoteOnへのポインタを返す) */
#MIDIEvent_CreateNoteOnNoteOn0 = MIDIData.MIDIEvent_CreateNoteOnNoteOn0
#MIDIEvent_CreateNoteOnNoteOn0.restype = c_void_p
#MIDIEvent_CreateNoteOnNoteOn0.argtypes = (c_void_p,)
# キーアフタータッチイベントの生成 */
#MIDIEvent_CreateKeyAftertouch = MIDIData.MIDIEvent_CreateKeyAftertouch
#MIDIEvent_CreateKeyAftertouch.restype = c_void_p
#MIDIEvent_CreateKeyAftertouch.argtypes = (c_void_p,)
# コントローラーイベントの生成 */
#MIDIEvent_CreateControlChange = MIDIData.MIDIEvent_CreateControlChange
#MIDIEvent_CreateControlChange.restype = c_void_p
#MIDIEvent_CreateControlChange.argtypes = (c_void_p,)
# RPNイベントの生成 */
# (CC#101+CC#100+CC#6の3イベントを生成し、CC#101へのポインタを返す) */
#MIDIEvent_CreateRPNChange = MIDIData.MIDIEvent_CreateRPNChange
#MIDIEvent_CreateRPNChange.restype = c_void_p
#MIDIEvent_CreateRPNChange.argtypes = (c_void_p,)
# NRPNイベントの生成 */
# (CC#99+CC#98+CC#6の3イベントを生成し、CC#99へのポインタを返す) */
#MIDIEvent_CreateNRPNChange = MIDIData.MIDIEvent_CreateNRPNChange
#MIDIEvent_CreateNRPNChange.restype = c_void_p
#MIDIEvent_CreateNRPNChange.argtypes = (c_void_p,)
# プログラムチェンジイベントの生成 */
#MIDIEvent_CreateProgramChange = MIDIData.MIDIEvent_CreateProgramChange
#MIDIEvent_CreateProgramChange.restype = c_void_p
#MIDIEvent_CreateProgramChange.argtypes = (c_void_p,)
# バンク・パッチイベントの生成 */
# (CC#0+CC#32+PCの3イベントを生成し、CC#0へのポインタを返す) */
#MIDIEvent_CreatePatchChange = MIDIData.MIDIEvent_CreatePatchChange
#MIDIEvent_CreatePatchChange.restype = c_void_p
#MIDIEvent_CreatePatchChange.argtypes = (c_void_p,)
# チャンネルアフタータッチイベントの生成 */
#MIDIEvent_CreateChannelAftertouch = MIDIData.MIDIEvent_CreateChannelAftertouch
#MIDIEvent_CreateChannelAftertouch.restype = c_void_p
#MIDIEvent_CreateChannelAftertouch.argtypes = (c_void_p,)
# ピッチベンドイベントの生成 */
#MIDIEvent_CreatePitchBend = MIDIData.MIDIEvent_CreatePitchBend
#MIDIEvent_CreatePitchBend.restype = c_void_p
#MIDIEvent_CreatePitchBend.argtypes = (c_void_p,)
# システムエクスクルーシヴイベントの生成 */
#MIDIEvent_CreateSysExEvent = MIDIData.MIDIEvent_CreateSysExEvent
#MIDIEvent_CreateSysExEvent.restype = c_void_p
#MIDIEvent_CreateSysExEvent.argtypes = (c_void_p,)
# メタイベントであるかどうかを調べる */
MIDIEvent_IsMetaEvent = MIDIData.MIDIEvent_IsMetaEvent
MIDIEvent_IsMetaEvent.restype = c_bool
MIDIEvent_IsMetaEvent.argtypes = (c_void_p,)
# シーケンス番号であるかどうかを調べる */
MIDIEvent_IsSequenceNumber = MIDIData.MIDIEvent_IsSequenceNumber
MIDIEvent_IsSequenceNumber.restype = c_bool
MIDIEvent_IsSequenceNumber.argtypes = (c_void_p,)
# テキストイベントであるかどうかを調べる */
MIDIEvent_IsTextEvent = MIDIData.MIDIEvent_IsTextEvent
MIDIEvent_IsTextEvent.restype = c_bool
MIDIEvent_IsTextEvent.argtypes = (c_void_p,)
# 著作権イベントであるかどうかを調べる */
MIDIEvent_IsCopyrightNotice = MIDIData.MIDIEvent_IsCopyrightNotice
MIDIEvent_IsCopyrightNotice.restype = c_bool
MIDIEvent_IsCopyrightNotice.argtypes = (c_void_p,)
# トラック名イベントであるかどうかを調べる */
MIDIEvent_IsTrackName = MIDIData.MIDIEvent_IsTrackName
MIDIEvent_IsTrackName.restype = c_bool
MIDIEvent_IsTrackName.argtypes = (c_void_p,)
# インストゥルメント名イベントであるかどうかを調べる */
MIDIEvent_IsInstrumentName = MIDIData.MIDIEvent_IsInstrumentName
MIDIEvent_IsInstrumentName.restype = c_bool
MIDIEvent_IsInstrumentName.argtypes = (c_void_p,)
# 歌詞イベントであるかどうかを調べる */
MIDIEvent_IsLyric = MIDIData.MIDIEvent_IsLyric
MIDIEvent_IsLyric.restype = c_bool
MIDIEvent_IsLyric.argtypes = (c_void_p,)
# マーカーイベントであるかどうかを調べる */
MIDIEvent_IsMarker = MIDIData.MIDIEvent_IsMarker
MIDIEvent_IsMarker.restype = c_bool
MIDIEvent_IsMarker.argtypes = (c_void_p,)
# キューポイントイベントであるかどうかを調べる */
MIDIEvent_IsCuePoint = MIDIData.MIDIEvent_IsCuePoint
MIDIEvent_IsCuePoint.restype = c_bool
MIDIEvent_IsCuePoint.argtypes = (c_void_p,)
# プログラム名イベントであるかどうかを調べる */
MIDIEvent_IsProgramName = MIDIData.MIDIEvent_IsProgramName
MIDIEvent_IsProgramName.restype = c_bool
MIDIEvent_IsProgramName.argtypes = (c_void_p,)
# デバイス名イベントであるかどうかを調べる */
MIDIEvent_IsDeviceName = MIDIData.MIDIEvent_IsDeviceName
MIDIEvent_IsDeviceName.restype = c_bool
MIDIEvent_IsDeviceName.argtypes = (c_void_p,)
# チャンネルプレフィックスイベントであるかどうかを調べる */
MIDIEvent_IsChannelPrefix = MIDIData.MIDIEvent_IsChannelPrefix
MIDIEvent_IsChannelPrefix.restype = c_bool
MIDIEvent_IsChannelPrefix.argtypes = (c_void_p,)
# ポートプレフィックスイベントであるかどうかを調べる */
MIDIEvent_IsPortPrefix = MIDIData.MIDIEvent_IsPortPrefix
MIDIEvent_IsPortPrefix.restype = c_bool
MIDIEvent_IsPortPrefix.argtypes = (c_void_p,)
# エンドオブトラックイベントであるかどうかを調べる */
MIDIEvent_IsEndofTrack = MIDIData.MIDIEvent_IsEndofTrack
MIDIEvent_IsEndofTrack.restype = c_bool
MIDIEvent_IsEndofTrack.argtypes = (c_void_p,)
# テンポイベントであるかどうかを調べる */
MIDIEvent_IsTempo = MIDIData.MIDIEvent_IsTempo
MIDIEvent_IsTempo.restype = c_bool
MIDIEvent_IsTempo.argtypes = (c_void_p,)
# SMPTEオフセットイベントであるかどうかを調べる */
MIDIEvent_IsSMPTEOffset = MIDIData.MIDIEvent_IsSMPTEOffset
MIDIEvent_IsSMPTEOffset.restype = c_bool
MIDIEvent_IsSMPTEOffset.argtypes = (c_void_p,)
# 拍子記号イベントであるかどうかを調べる */
MIDIEvent_IsTimeSignature = MIDIData.MIDIEvent_IsTimeSignature
MIDIEvent_IsTimeSignature.restype = c_bool
MIDIEvent_IsTimeSignature.argtypes = (c_void_p,)
# 調性記号イベントであるかどうかを調べる */
MIDIEvent_IsKeySignature = MIDIData.MIDIEvent_IsKeySignature
MIDIEvent_IsKeySignature.restype = c_bool
MIDIEvent_IsKeySignature.argtypes = (c_void_p,)
# シーケンサ独自のイベントであるかどうかを調べる */
MIDIEvent_IsSequencerSpecific = MIDIData.MIDIEvent_IsSequencerSpecific
MIDIEvent_IsSequencerSpecific.restype = c_bool
MIDIEvent_IsSequencerSpecific.argtypes = (c_void_p,)
# MIDIイベントであるかどうかを調べる */
MIDIEvent_IsMIDIEvent = MIDIData.MIDIEvent_IsMIDIEvent
MIDIEvent_IsMIDIEvent.restype = c_bool
MIDIEvent_IsMIDIEvent.argtypes = (c_void_p,)
# ノートオンイベントであるかどうかを調べる */
# (ノートオンイベントでベロシティ0のものはノートオフイベントとみなす。以下同様) */
MIDIEvent_IsNoteOn = MIDIData.MIDIEvent_IsNoteOn
MIDIEvent_IsNoteOn.restype = c_bool
MIDIEvent_IsNoteOn.argtypes = (c_void_p,)
# ノートオフイベントであるかどうかを調べる */
MIDIEvent_IsNoteOff = MIDIData.MIDIEvent_IsNoteOff
MIDIEvent_IsNoteOff.restype = c_bool
MIDIEvent_IsNoteOff.argtypes = (c_void_p,)
# ノートイベントであるかどうかを調べる */
MIDIEvent_IsNote = MIDIData.MIDIEvent_IsNote
MIDIEvent_IsNote.restype = c_bool
MIDIEvent_IsNote.argtypes = (c_void_p,)
# NOTEONOTEOFFイベントであるかどうかを調べる */
# これはノートオン(0x9n)とノートオフ(0x8n)が結合イベントしたイベントでなければならない。 */
MIDIEvent_IsNoteOnNoteOff = MIDIData.MIDIEvent_IsNoteOnNoteOff
MIDIEvent_IsNoteOnNoteOff.restype = c_bool
MIDIEvent_IsNoteOnNoteOff.argtypes = (c_void_p,)
# NOTEONNOTEON0イベントであるかどうかを調べる */
# これはノートオン(0x9n)とノートオフ(0x9n,vel==0)が結合イベントしたイベントでなければならない。 */
MIDIEvent_IsNoteOnNoteOn0 = MIDIData.MIDIEvent_IsNoteOnNoteOn0
MIDIEvent_IsNoteOnNoteOn0.restype = c_bool
MIDIEvent_IsNoteOnNoteOn0.argtypes = (c_void_p,)
# キーアフタータッチイベントであるかどうかを調べる */
MIDIEvent_IsKeyAftertouch = MIDIData.MIDIEvent_IsKeyAftertouch
MIDIEvent_IsKeyAftertouch.restype = c_bool
MIDIEvent_IsKeyAftertouch.argtypes = (c_void_p,)
# コントロールチェンジイベントであるかどうかを調べる */
MIDIEvent_IsControlChange = MIDIData.MIDIEvent_IsControlChange
MIDIEvent_IsControlChange.restype = c_bool
MIDIEvent_IsControlChange.argtypes = (c_void_p,)
# RPNチェンジイベントであるかどうかを調べる */
MIDIEvent_IsRPNChange = MIDIData.MIDIEvent_IsRPNChange
MIDIEvent_IsRPNChange.restype = c_bool
MIDIEvent_IsRPNChange.argtypes = (c_void_p,)
# NRPNチェンジイベントであるかどうかを調べる */
MIDIEvent_IsNRPNChange = MIDIData.MIDIEvent_IsNRPNChange
MIDIEvent_IsNRPNChange.restype = c_bool
MIDIEvent_IsNRPNChange.argtypes = (c_void_p,)
# プログラムチェンジイベントであるかどうかを調べる */
MIDIEvent_IsProgramChange = MIDIData.MIDIEvent_IsProgramChange
MIDIEvent_IsProgramChange.restype = c_bool
MIDIEvent_IsProgramChange.argtypes = (c_void_p,)
# パッチチェンジイベントであるかどうかを調べる */
MIDIEvent_IsPatchChange = MIDIData.MIDIEvent_IsPatchChange
MIDIEvent_IsPatchChange.restype = c_bool
MIDIEvent_IsPatchChange.argtypes = (c_void_p,)
# チャンネルアフタータッチイベントであるかどうかを調べる */
MIDIEvent_IsChannelAftertouch = MIDIData.MIDIEvent_IsChannelAftertouch
MIDIEvent_IsChannelAftertouch.restype = c_bool
MIDIEvent_IsChannelAftertouch.argtypes = (c_void_p,)
# ピッチベンドイベントであるかどうかを調べる */
MIDIEvent_IsPitchBend = MIDIData.MIDIEvent_IsPitchBend
MIDIEvent_IsPitchBend.restype = c_bool
MIDIEvent_IsPitchBend.argtypes = (c_void_p,)
# システムエクスクルーシヴイベントであるかどうかを調べる */
MIDIEvent_IsSysExEvent = MIDIData.MIDIEvent_IsSysExEvent
MIDIEvent_IsSysExEvent.restype = c_bool
MIDIEvent_IsSysExEvent.argtypes = (c_void_p,)
# 浮遊イベントであるかどうか調べる */
MIDIEvent_IsFloating = MIDIData.MIDIEvent_IsFloating
MIDIEvent_IsFloating.restype = c_bool
MIDIEvent_IsFloating.argtypes = (c_void_p,)
# 結合イベントであるかどうか調べる */
MIDIEvent_IsCombined = MIDIData.MIDIEvent_IsCombined
MIDIEvent_IsCombined.restype = c_bool
MIDIEvent_IsCombined.argtypes = (c_void_p,)
# イベントの種類を取得 */
MIDIEvent_GetKind = MIDIData.MIDIEvent_GetKind
MIDIEvent_GetKind.restype = c_uint
MIDIEvent_GetKind.argtypes = (c_void_p,)
# イベントの種類を設定 */
#MIDIEvent_SetKind = MIDIData.MIDIEvent_SetKind
#MIDIEvent_SetKind.restype = c_void_p
#MIDIEvent_SetKind.argtypes = (c_void_p,)
# イベントの長さ取得 */
#MIDIEvent_GetLen = MIDIData.MIDIEvent_GetLen
#MIDIEvent_GetLen.restype = c_void_p
#MIDIEvent_GetLen.argtypes = (c_void_p,)
# イベントのデータ部を取得 */
MIDIEvent_GetData = MIDIData.MIDIEvent_GetData
MIDIEvent_GetData.restype = c_uint
MIDIEvent_GetData.argtypes = (c_void_p,c_wchar_p,c_uint,)
# イベントのデータ部を設定(この関数は大変危険です。整合性のチェキはしません) */
#MIDIEvent_SetData = MIDIData.MIDIEvent_SetData
#MIDIEvent_SetData.restype = c_void_p
#MIDIEvent_SetData.argtypes = (c_void_p,)
# イベントの文字コードを取得(テキスト・著作権・トラック名・インストゥルメント名・ */
# 歌詞・マーカー・キューポイント・プログラム名・デバイス名のみ) */
#MIDIEvent_GetCharCode = MIDIData.MIDIEvent_GetCharCode
#MIDIEvent_GetCharCode.restype = c_void_p
#MIDIEvent_GetCharCode.argtypes = (c_void_p,)
# イベントの文字コードを設定(テキスト・著作権・トラック名・インストゥルメント名・ */
# 歌詞・マーカー・キューポイント・プログラム名・デバイス名のみ) */
#MIDIEvent_SetCharCode = MIDIData.MIDIEvent_SetCharCode
#MIDIEvent_SetCharCode.restype = c_void_p
#MIDIEvent_SetCharCode.argtypes = (c_void_p,)
# イベントのテキストを取得(テキスト・著作権・トラック名・インストゥルメント名・ */
# 歌詞・マーカー・キューポイント・プログラム名・デバイス名のみ) */
#MIDIEvent_GetText = MIDIData.MIDIEvent_GetTextW
#MIDIEvent_GetText.restype = c_void_p
#MIDIEvent_GetText.argtypes = (c_void_p,)
# イベントのテキストを設定(テキスト・著作権・トラック名・インストゥルメント名・ */
# 歌詞・マーカー・キューポイント・プログラム名・デバイス名のみ) */
#MIDIEvent_SetText = MIDIData.MIDIEvent_SetTextW
#MIDIEvent_SetText.restype = c_void_p
#MIDIEvent_SetText.argtypes = (c_void_p,)
# SMPTEオフセットの取得(SMPTEオフセットイベントのみ) */
#MIDIEvent_GetSMPTEOffset = MIDIData.MIDIEvent_GetSMPTEOffset
#MIDIEvent_GetSMPTEOffset.restype = c_void_p
#MIDIEvent_GetSMPTEOffset.argtypes = (c_void_p,)
# SMPTEオフセットの設定(SMPTEオフセットイベントのみ) */
#MIDIEvent_SetSMPTEOffset = MIDIData.MIDIEvent_SetSMPTEOffset
#MIDIEvent_SetSMPTEOffset.restype = c_void_p
#MIDIEvent_SetSMPTEOffset.argtypes = (c_void_p,)
# テンポ取得(テンポイベントのみ) */
MIDIEvent_GetTempo = MIDIData.MIDIEvent_GetTempo
MIDIEvent_GetTempo.restype = c_uint
MIDIEvent_GetTempo.argtypes = (c_void_p,)
# テンポ設定(テンポイベントのみ) */
MIDIEvent_SetTempo = MIDIData.MIDIEvent_SetTempo
MIDIEvent_SetTempo.restype = c_bool
MIDIEvent_SetTempo.argtypes = (c_void_p,c_uint,)
# 拍子記号取得(拍子記号イベントのみ) */
#MIDIEvent_GetTimeSignature = MIDIData.MIDIEvent_GetTimeSignature
#MIDIEvent_GetTimeSignature.restype = c_void_p
#MIDIEvent_GetTimeSignature.argtypes = (c_void_p,)
# 拍子記号の設定(拍子記号イベントのみ) */
#MIDIEvent_SetTimeSignature = MIDIData.MIDIEvent_SetTimeSignature
#MIDIEvent_SetTimeSignature.restype = c_void_p
#MIDIEvent_SetTimeSignature.argtypes = (c_void_p,)
# 調性記号の取得(調性記号イベントのみ) */
#MIDIEvent_GetKeySignature = MIDIData.MIDIEvent_GetKeySignature
#MIDIEvent_GetKeySignature.restype = c_void_p
#MIDIEvent_GetKeySignature.argtypes = (c_void_p,)
# 調性記号の設定(調性記号イベントのみ) */
#MIDIEvent_SetKeySignature = MIDIData.MIDIEvent_SetKeySignature
#MIDIEvent_SetKeySignature.restype = c_void_p
#MIDIEvent_SetKeySignature.argtypes = (c_void_p,)
# イベントのメッセージ取得(MIDIチャンネルイベント及びシステムエクスクルーシヴのみ) */
#MIDIEvent_GetMIDIMessage = MIDIData.MIDIEvent_GetMIDIMessage
#MIDIEvent_GetMIDIMessage.restype = c_void_p
#MIDIEvent_GetMIDIMessage.argtypes = (c_void_p,)
# イベントのメッセージ設定(MIDIチャンネルイベント及びシステムエクスクルーシヴのみ) */
#MIDIEvent_SetMIDIMessage = MIDIData.MIDIEvent_SetMIDIMessage
#MIDIEvent_SetMIDIMessage.restype = c_void_p
#MIDIEvent_SetMIDIMessage.argtypes = (c_void_p,)
# イベントのチャンネル取得(MIDIチャンネルイベントのみ) */
MIDIEvent_GetChannel = MIDIData.MIDIEvent_GetChannel
MIDIEvent_GetChannel.restype = c_uint
MIDIEvent_GetChannel.argtypes = (c_void_p,)
# イベントのチャンネル設定(MIDIチャンネルイベントのみ) */
MIDIEvent_SetChannel = MIDIData.MIDIEvent_SetChannel
MIDIEvent_SetChannel.restype = c_bool
MIDIEvent_SetChannel.argtypes = (c_void_p,c_uint,)
# イベントの時刻取得 */
MIDIEvent_GetTime = MIDIData.MIDIEvent_GetTime
MIDIEvent_GetTime.restype = c_uint
MIDIEvent_GetTime.argtypes = (c_void_p,)
# イベントの時刻設定 */
#MIDIEvent_SetTimeSingle = MIDIData.MIDIEvent_SetTimeSingle
#MIDIEvent_SetTimeSingle.restype = c_void_p
#MIDIEvent_SetTimeSingle.argtypes = (c_void_p,)
# イベントの時刻設定 */
MIDIEvent_SetTime = MIDIData.MIDIEvent_SetTime
MIDIEvent_SetTime.restype = c_uint
MIDIEvent_SetTime.argtypes = (c_void_p,c_uint,)
# イベントのキー取得(ノートオフ・ノートオン・チャンネルアフターのみ) */
MIDIEvent_GetKey = MIDIData.MIDIEvent_GetKey
MIDIEvent_GetKey.restype = c_uint
MIDIEvent_GetKey.argtypes = (c_void_p,)
# イベントのキー設定(ノートオフ・ノートオン・チャンネルアフターのみ) */
MIDIEvent_SetKey = MIDIData.MIDIEvent_SetKey
MIDIEvent_SetKey.restype = c_uint
MIDIEvent_SetKey.argtypes = (c_void_p,c_uint,)
# イベントのベロシティ取得(ノートオフ・ノートオンのみ) */
MIDIEvent_GetVelocity = MIDIData.MIDIEvent_GetVelocity
MIDIEvent_GetVelocity.restype = c_uint
MIDIEvent_GetVelocity.argtypes = (c_void_p,)
# イベントのベロシティ設定(ノートオフ・ノートオンのみ) */
MIDIEvent_SetVelocity = MIDIData.MIDIEvent_SetVelocity
MIDIEvent_SetVelocity.restype = c_bool
MIDIEvent_SetVelocity.argtypes = (c_void_p,c_uint,)
# 結合イベントの音長さ取得(ノートのみ) */
MIDIEvent_GetDuration = MIDIData.MIDIEvent_GetDuration
MIDIEvent_GetDuration.restype = c_uint
MIDIEvent_GetDuration.argtypes = (c_void_p,)
# 結合イベントの音長さ設定(ノートのみ) */
MIDIEvent_SetDuration = MIDIData.MIDIEvent_SetDuration
MIDIEvent_SetDuration.restype = c_bool
MIDIEvent_SetDuration.argtypes = (c_void_p,c_uint,)
# 結合イベントのバンク取得(RPNチェンジ・NRPNチェンジ・パッチチェンジのみ) */
#MIDIEvent_GetBank = MIDIData.MIDIEvent_GetBank
#MIDIEvent_GetBank.restype = c_void_p
#MIDIEvent_GetBank.argtypes = (c_void_p,)
# 結合イベントのバンク上位(MSB)取得(RPNチェンジ・NRPNチェンジ・パッチチェンジのみ) */
#MIDIEvent_GetBankMSB = MIDIData.MIDIEvent_GetBankMSB
#MIDIEvent_GetBankMSB.restype = c_void_p
#MIDIEvent_GetBankMSB.argtypes = (c_void_p,)
# 結合イベントのバンク下位(LSB)取得(RPNチェンジ・NRPNチェンジ・パッチチェンジのみ) */
#MIDIEvent_GetBankLSB = MIDIData.MIDIEvent_GetBankLSB
#MIDIEvent_GetBankLSB.restype = c_void_p
#MIDIEvent_GetBankLSB.argtypes = (c_void_p,)
# 結合イベントのバンク設定(RPNチェンジ・NRPNチェンジ・パッチチェンジのみ) */
#MIDIEvent_SetBank = MIDIData.MIDIEvent_SetBank
#MIDIEvent_SetBank.restype = c_void_p
#MIDIEvent_SetBank.argtypes = (c_void_p,)
# 結合イベントのバンク上位(MSB)設定(RPNチェンジ・NRPNチェンジ・パッチチェンジのみ) */
#MIDIEvent_SetBankMSB = MIDIData.MIDIEvent_SetBankMSB
#MIDIEvent_SetBankMSB.restype = c_void_p
#MIDIEvent_SetBankMSB.argtypes = (c_void_p,)
# 結合イベントのバンク下位(LSB)設定(RPNチェンジ・NRPNチェンジ・パッチチェンジのみ) */
#MIDIEvent_SetBankLSB = MIDIData.MIDIEvent_SetBankLSB
#MIDIEvent_SetBankLSB.restype = c_void_p
#MIDIEvent_SetBankLSB.argtypes = (c_void_p,)
# 結合イベントのプログラムナンバーを取得(パッチイベントのみ) */
#MIDIEvent_GetPatchNum = MIDIData.MIDIEvent_GetPatchNum
#MIDIEvent_GetPatchNum.restype = c_void_p
#MIDIEvent_GetPatchNum.argtypes = (c_void_p,)
# 結合イベントのプログラムナンバーを設定(パッチイベントのみ) */
#MIDIEvent_SetPatchNum = MIDIData.MIDIEvent_SetPatchNum
#MIDIEvent_SetPatchNum.restype = c_void_p
#MIDIEvent_SetPatchNum.argtypes = (c_void_p,)
# 結合イベントのデータエントリーMSBを取得(RPNチェンジ・NPRNチェンジのみ) */
#MIDIEvent_GetDataEntryMSB = MIDIData.MIDIEvent_GetDataEntryMSB
#MIDIEvent_GetDataEntryMSB.restype = c_void_p
#MIDIEvent_GetDataEntryMSB.argtypes = (c_void_p,)
# 結合イベントのデータエントリーMSBを設定(RPNチェンジ・NPRNチェンジのみ) */
#MIDIEvent_SetDataEntryMSB = MIDIData.MIDIEvent_SetDataEntryMSB
#MIDIEvent_SetDataEntryMSB.restype = c_void_p
#MIDIEvent_SetDataEntryMSB.argtypes = (c_void_p,)
# イベントの番号取得(コントロールチェンジ・プログラムチェンジのみ) */
MIDIEvent_GetNumber = MIDIData.MIDIEvent_GetNumber
MIDIEvent_GetNumber.restype = c_uint
MIDIEvent_GetNumber.argtypes = (c_void_p,)
# イベントの番号設定(コントロールチェンジ・プログラムチェンジのみ) */
MIDIEvent_SetNumber = MIDIData.MIDIEvent_SetNumber
MIDIEvent_SetNumber.restype = c_uint
MIDIEvent_SetNumber.argtypes = (c_void_p,c_uint,)
# イベントの値取得(キーアフター・コントローラー・チャンネルアフター・ピッチベンド) */
MIDIEvent_GetValue = MIDIData.MIDIEvent_GetValue
MIDIEvent_GetValue.restype = c_uint
MIDIEvent_GetValue.argtypes = (c_void_p,)
# イベントの値設定(キーアフター・コントローラー・チャンネルアフター・ピッチベンド) */
MIDIEvent_SetValue = MIDIData.MIDIEvent_SetValue
MIDIEvent_SetValue.restype = c_uint
MIDIEvent_SetValue.argtypes = (c_void_p,c_uint,)
# 次のイベントへのポインタを取得(なければNULL) */
MIDIEvent_GetNextEvent = MIDIData.MIDIEvent_GetNextEvent
MIDIEvent_GetNextEvent.restype = c_void_p
MIDIEvent_GetNextEvent.argtypes = (c_void_p,)
# 前のイベントへのポインタを取得(なければNULL) */
MIDIEvent_GetPrevEvent = MIDIData.MIDIEvent_GetPrevEvent
MIDIEvent_GetPrevEvent.restype = c_void_p
MIDIEvent_GetPrevEvent.argtypes = (c_void_p,)
# 次の同種のイベントへのポインタを取得(なければNULL) */
MIDIEvent_GetNextSameKindEvent = MIDIData.MIDIEvent_GetNextSameKindEvent
MIDIEvent_GetNextSameKindEvent.restype = c_void_p
MIDIEvent_GetNextSameKindEvent.argtypes = (c_void_p,)
# 前の同種のイベントへのポインタを取得(なければNULL) */
MIDIEvent_GetPrevSameKindEvent = MIDIData.MIDIEvent_GetPrevSameKindEvent
MIDIEvent_GetPrevSameKindEvent.restype = c_void_p
MIDIEvent_GetPrevSameKindEvent.argtypes = (c_void_p,)
# 親トラックへのポインタを取得(なければNULL) */
MIDIEvent_GetParent = MIDIData.MIDIEvent_GetParent
MIDIEvent_GetParent.restype = c_void_p
MIDIEvent_GetParent.argtypes = (c_void_p,)
# イベントの内容を文字列表現に変換 */
#MIDIEvent_ToStringEx = MIDIData.MIDIEvent_ToStringExW
#MIDIEvent_ToStringEx.restype = c_void_p
#MIDIEvent_ToStringEx.argtypes = (c_void_p,)
# イベンの内容トを文字列表現に変換 */
#MIDIEvent_ToString = MIDIData.MIDIEvent_ToStringW
#MIDIEvent_ToString.restype = c_void_p
#MIDIEvent_ToString.argtypes = (c_void_p,)
