import torch

# 1. Comprueba si CUDA está disponible
cuda_disponible = torch.cuda.is_available()
print(f"CUDA disponible: {cuda_disponible}")

if cuda_disponible:
    # 2. Muestra el número de GPUs detectadas
    num_gpus = torch.cuda.device_count()
    print(f"Número de GPUs: {num_gpus}")

    # 3. Muestra el nombre de la primera GPU
    nombre_gpu = torch.cuda.get_device_name(0)
    print(f"Nombre de la GPU (0): {nombre_gpu}")

    # 4. (Opcional) Crea un tensor y muévelo a la GPU
    x = torch.rand(5, 3)
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    x = x.to(device)
    print(f"\nTensor en el dispositivo: {x.device}")
else:
    print("PyTorch no detectó soporte CUDA o no se instaló la versión correcta.")