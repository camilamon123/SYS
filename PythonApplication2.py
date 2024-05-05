
import numpy as np
import matplotlib.pyplot as plt
import wave

from scipy.fft import fft

#Cargar archivo de audio

audio = wave.open(r'C:\Users\Administrador\Downloads\Facultad\sys\TP\audio.wav', "rb" )

#obtener variables

#sample_freq = audio.getframerate()
frecuencia = audio.getframerate()
n_samples = audio.getnframes()
signal_wave = audio.readframes(-1)  #amplitud

#print('frecuencia', frecuencia )
audio.close() # cierro archivo 
#duración del audio 

audio_duration = n_samples / frecuencia #duracion

#signal array 

signal_array = np.frombuffer(signal_wave, dtype= np.int16)
times = np.linspace(0,audio_duration, num = n_samples)*1000

#Graficar señal de audio

plt.figure(figsize=(15,5))
plt.plot(times , signal_array/100,color = "black",linewidth=1)

#fonema a
#inicio_a = 179*100
#final_a = 182*100
#plt.plot(times[inicio_a:final_a], signal_array[inicio_a:final_a]/100, color='red', label= 'Fonema a')

#fonema a2
#inicio_a2 = 308*100
#final_a2 = 311*100
#plt.plot(times[inicio_a2:final_a2], signal_array[inicio_a2:final_a2]/100, color='red')

#fonema s
#inicio_s = 242*100
#final_s = 305*100
#plt.plot(times[inicio_s:final_s], signal_array[inicio_s:final_s]/100, color='purple', label= 'Fonema s ')

#fonema i 

#inicio_e = 44*100
#final_e = 46*100
#plt.plot(times[inicio_e:final_e], signal_array[inicio_e:final_e]/100, color='b',linewidth=0.5)


#plt.legend(loc='lower right')
#plt.title("Señal de voz de ""Mikasa"" ")


#---------------------------------SEÑALES PERIODICAS Y APERIODICAS
#periodicas:

#inicio_a = 0
#final_a = 106*100
#plt.plot(times[inicio_a:final_a], signal_array[inicio_a:final_a]/100, color='black', label= 'Periodica', linewidth=0.5)

#inicio_c = 177*100
#final_c = 243*100
#plt.plot(times[inicio_c:final_c], signal_array[inicio_c:final_c]/100, color='black', linewidth=0.5)

#inicio_d = 305*100
#final_d = 350*100
#plt.plot(times[inicio_d:final_d], signal_array[inicio_d:final_d]/100, color='black',linewidth=0.5)

#aperiodicas:

#inicio_b = 106*100
#final_b = 177*100
#plt.plot(times[inicio_b:final_b], signal_array[inicio_b:final_b]/100, color='b', label= 'Aperiodica', linewidth=0.5)

#inicio_d = 243*100
#final_d = 305*100
#plt.plot(times[inicio_d:final_d], signal_array[inicio_d:final_d]/100, color='b',linewidth=0.5)

#inicio_e = 350*100
#final_e = 500*100
#plt.plot(times[inicio_e:final_e], signal_array[inicio_e:final_e]/100, color='b',linewidth=0.5)

#plt.legend(loc='lower right')

#plt.xticks(range(800))
#plt.xlim(700,730)

#plt.yticks(range(100)*10)
#plt.ylim(-150,150)

plt.xlim(0,(audio_duration)*1000 - 400 )
#plt.xlim(700,800)
#plt.ylim(-150,150)
plt.ylabel("Amplitud [dB]", color = "red")
plt.xlabel("Tiempo en ms", color = "red")
plt.grid()
#plt.savefig('señal_i2.png') #guardar imagen
plt.show()




#AUTOCORRELACIÓN 

# Calcular la autocorrelación
#autocorr = sm.tsa.acf(signal_array)

# Imprimir la autocorrelación
#print(autocorr)

# Graficar la función de autocorrelación
#fig = tsaplots.plot_acf(signal_array, lags=10)
#plt.show()


# Calcular la FFT



#xf = np.linspace(45.5, 46)
#x_f = np.linspace(693, 730, signal_array.size//2)
# Graficar la FFT
#plt.plot(np.abs(yf))
# Calcula la FFT de la señal de audio
#fft_result = np.fft.fft(signal_array)

# Calcula las frecuencias correspondientes
#T = (1/(np.fft.fftfreq(len(signal_array), 1))) #periodos
#frequencies = ((np.fft.fftfreq(2, 1)))*1000 #periodos
# Grafica los coeficientes de Fourier
#plt.plot(frequencies, np.abs(fft_result), color = 'm', linewidth=0.5)
#time = [0 , (len(signal_array) - 1)*T]
#plt.plot(time, np.abs(fft_result), color = 'm', linewidth=0.5)
#plt.plot(times, np.abs(fft_result), color = 'm', linewidth=0.5)
#plt.xlim(0,200)
#plt.xlabel('Tiempo (us)')
#plt.ylabel('Magnitud')
#plt.title('Coeficientes de Fourier del fonema I')
#plt.grid(True)
#plt.show()

# Encontrar la frecuencia dominante
#idx = np.argmax(np.abs(yf))
#freq = 1/xf[idx]
#print('Frecuencia dominante:', freq, 'Hz')

# Calcular el período
#periodo = 1/freq
#print('Período:', periodo, 's')
# Graficamos los coeficientes de Fourier
