from main.py import * 


PATH = 'my_model.pth' 
model = torch.load(PATH)
model.eval()

pred = model(get_ith_fileget_ith_file(15, 'data/bronze_layer'))
print(pred)

