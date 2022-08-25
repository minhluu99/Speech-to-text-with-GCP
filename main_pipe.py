from Process_Pipeline import *
from Process_F import *

def Init_Pipeline(Audio_addr):
    audio = AudioSegment.from_file(Audio_addr)
    aPipeline = Tree_audio()
    aPipeline.floor = 'Audio'
    aPipeline.info = {'Audio_addr' : Audio_addr}
    aPipeline.start = 0
    aPipeline.end = len(audio)
    return aPipeline

def Func_Pipeline(aPipeline,Split_Function,set_channel=False,**para):
    idx = 0
    floor = aPipeline.get_floor_name()
    while f'{Split_Function.__name__}_{idx}' in floor:
        idx += 1
    floor = f'{Split_Function.__name__}_{idx}'
    audio = aPipeline.info['Audio_addr']
    audio = AudioSegment.from_file(audio,'wav')
    if set_channel == True:
        audio.set_channels(1)
    silence = 0
    for Audio_Node in aPipeline.get_floor(-1):
        # Xử lý cắt audio để không mất chữ
        # Bắt đầu sớm hơn nếu có silence trước đó
        start = Audio_Node.start
        if silence == 0 and start != 0 and Audio_Node.silence != None:
            start = 0
        elif silence != 0:
            start -= silence * 1/3
        else:
            pass
        # Dừng trễ hơn nếu có silence
        end = Audio_Node.end
        if Audio_Node.silence != None:
            silence = Audio_Node.silence[1] - Audio_Node.silence[0]
            end = end + silence * 1/3
        audio_sample = audio[start:end]
        addr_audio_sample = 'Processing.wav'
        audio_sample.export(addr_audio_sample,'wav')
        Splited_List = Split_Function(addr_audio_sample,**para)

        for eledict in Splited_List:
            new_Audio_node = Tree_audio()
            new_Audio_node.start = eledict.pop('Start') + start
            new_Audio_node.end = eledict.pop('End') + start
            sil = eledict.pop('Silence')
            sil = (sil[0] + start , sil[1] + start)
            new_Audio_node.silence = sil
            if 'Speaker' in list(eledict):
                new_Audio_node.info = {'Speaker':eledict.pop('Speaker')}
            new_Audio_node.other = eledict
            new_Audio_node.floor = floor
            Audio_Node.children.append(new_Audio_node)


if __name__ == '__main__':
    Pipeline = Init_Pipeline('Input/23-06-2022 14 12 36.wav')

    Func_Pipeline(Pipeline,Split_speaker,set_channel=False)
    Func_Pipeline(Pipeline,Split_silence,set_channel=False)

    info,HashList = Pipeline.prepare_to_S2t(-1,set_channels = True)

    S2t(HashList)
    StringList = S2t_get_str(HashList)
    S2t_filter(StringList)
    S2t_print(StringList)