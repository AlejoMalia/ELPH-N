import numpy as np
rng=np.random.default_rng(7)

# MATEMATICA (antes de correr):
#  multi-step con n posiciones -> los armonicos multiplo de n NO se separan (HSP).
#  M3' usa n=4 (0/90/180/270)  -> ciego a 4t, 8t, 12t...
#  Una bandeja rectangular fresada en 3 ejes ortogonales tiene error de
#  PERPENDICULARIDAD y desajuste de escala X/Y = componente 4t DOMINANTE.
#  PREDICCION: con n=4, el 4t de la PLACA se le atribuye entero a la CAMARA.
#              con n=7 (primo), se recupera.

NB, TH = 25, np.linspace(0,2*np.pi,25,endpoint=False)
placa  = 1.0*np.cos(4*TH) + 0.4*np.cos(2*TH) + 0.3*np.cos(3*TH)   # um, 4t dominante
camara = 0.6*np.cos(4*TH+1.1) + 0.5*np.cos(1*TH)                  # um, fijo en el lab

def separa(n, reps=1):
    """multi-step: se gira la placa n pasos iguales; la camara no gira."""
    S=[]
    for k in range(n):
        p = np.roll(placa, int(round(k*NB/n)))      # la placa ROTA con la bandeja
        S.append(np.mean([p + camara + rng.normal(0,0.02,NB) for _ in range(reps)],axis=0))
    est_cam = np.mean(S,axis=0)                      # la media mata lo que rota... salvo multiplos de n
    est_pla = S[0] - est_cam
    return est_pla, est_cam

def amp4(x):  return abs(np.fft.rfft(x)[4])/NB*2

print(f"  VERDAD    placa |4t| = {amp4(placa):.3f} um     camara |4t| = {amp4(camara):.3f} um\n")
for n,reps in ((4,5),(5,4),(7,3),(20,1)):
    ep,ec = separa(n,reps)
    err_p = np.sqrt(np.mean((ep-placa+np.mean(placa))**2))
    print(f"  n={n:2d} x{reps}  ({n*reps} disparos)   |4t| placa estimado = {amp4(ep):.3f}  "
          f"camara = {amp4(ec):.3f}   {'<- CIEGO al 4t' if n%4==0 else 'ok'}")
