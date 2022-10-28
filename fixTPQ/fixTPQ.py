import sys
import os
import statistics
exec(open("./MIDIData.py",encoding='utf-8').read())

if len(sys.argv) < 2:
	sys.exit()
elif not sys.argv[1].endswith('.mid') or not os.path.isfile(sys.argv[1]):
	sys.exit()


gates = []
pMIDIData = MIDIData_LoadFromSMF(sys.argv[1])
tr=MIDIData_GetTimeResolution(pMIDIData)
pMIDITrack = MIDIData_GetFirstTrack(pMIDIData)
while pMIDITrack:
	pMIDIEvent = MIDITrack_GetFirstEvent(pMIDITrack)
	while pMIDIEvent:
		if MIDIEvent_GetKind(pMIDIEvent) >> 4 << 4 == MIDIEVENT_NOTEON:
			if MIDIEvent_GetVelocity(pMIDIEvent) != 0:
				MIDIEvent_Combine(pMIDIEvent)
				pNEXTEvent = MIDIEvent_GetNextSameKindEvent(pMIDIEvent)
				if pNEXTEvent is not None:
					d=MIDIEvent_GetTime(pNEXTEvent)-MIDIEvent_GetTime(pMIDIEvent)
					if d != 0:
						gates.append(d)
		pMIDIEvent = MIDIEvent_GetNextEvent(pMIDIEvent)
	pMIDITrack = MIDITrack_GetNextTrack(pMIDITrack)
MIDIData_Delete(pMIDIData)

print('現在の解像度	: '+str(tr))
print('最頻出		: ' + str(statistics.mode(gates)))
print('全要素		: ' + str(sorted(list(set(gates)))))

TPQ = input('新しい解像度	: ')
try:
	TPQ = int(TPQ)
	f = open(sys.argv[1],'rb')
	b = f.read()
	ba = bytearray(b)
	f.close()
	fn=sys.argv[1][:-4]+'_'+str(TPQ)+'TPQ'+'.mid'
	f = open(fn,'xb')
	ba[0xD] = TPQ
	f.write(ba)
	f.close()
	pMIDIData = MIDIData_LoadFromSMF(fn)
	pMIDITrack = MIDIData_GetFirstTrack(pMIDIData)
	while pMIDITrack:
		pMIDIEvent = MIDITrack_GetFirstEvent(pMIDITrack)
		while pMIDIEvent:
			if MIDIEvent_IsTempo(pMIDIEvent):
				MIDIEvent_SetTempo(pMIDIEvent,int(MIDIEvent_GetTempo(pMIDIEvent)*TPQ/tr))
			pMIDIEvent = MIDIEvent_GetNextEvent(pMIDIEvent)
		pMIDITrack = MIDITrack_GetNextTrack(pMIDITrack)
	MIDIData_SaveAsSMF(pMIDIData,fn)
	MIDIData_Delete(pMIDIData)
except ValueError:
	print('無効な入力です。')

