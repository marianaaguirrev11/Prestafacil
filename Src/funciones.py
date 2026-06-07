from datetime import date
from reportlab.pdfgen import canvas
#VALIDACIONES DE USUARIO

def ValidarNombreApellido(nombre:str)->bool:
    #Longitud no puede tener menos de tres letras 
    #no puede tener numeros
    longitud= len(nombre)
    if longitud >= 3:
        #la longitud ta ok, ya puedo validar los numeros
        #validador= True
        numeros = '0123456789'
        for letra in nombre:
            if letra in numeros:
                return False 
        return True
    else:
        return False
    
def GenerarID(categoria, contador):

    if categoria == '1':
        prefijo = 'VID'

    elif categoria == '2':
        prefijo = 'LIB'

    elif categoria == '3':
        prefijo = 'MUV'

    elif categoria == '4':
        prefijo = 'HER'

    elif categoria == '5':
        prefijo = 'DIN'

    else:
        prefijo = 'MIS'

    return prefijo + str(contador)

def ValidarCedula(cedula:str)->bool:
    longitud = len(cedula)
    if longitud >= 3 and longitud <= 15:
        #puedo validar que todos sean digitos 
        if cedula.isnumeric():
            return True
        else:
            return False
    else:
        return False

def ValidarCorreo(correo):
    if '@' not in correo:
        return False
    
    partes = correo.split('@')
    if len(partes) !=2:
        return False
    
    usuario = partes[0]
    servidor_y_dominio= partes[1]
    
    if usuario == '':
        return False
    
    if '.' not in servidor_y_dominio:
        return False
    
    partes_servidor= servidor_y_dominio.split('.')
    
    for parte in partes_servidor:
        if parte == '':
            return False
        
    return True 

def ValidarTiempoPrestamo(dias):
    if dias==5 or dias==10 or dias==15 or dias==30:
        return True
    else:
        return False
    
def ObtenerFechaActual():
    hoy = date.today()
    return str(hoy)
    
    #generacion archivo (.pdf)
def GenerarCertificadoDevolucion(nombre_usuario, id_item, fecha_dev):

    nombre_archivo = f"{nombre_usuario}_{fecha_dev}_{id_item}.pdf"

    pdf = canvas.Canvas(nombre_archivo)

    pdf.drawString(50, 800, "--------------------------------------------------")
    pdf.drawString(50, 780, "CERTIFICADO DE DEVOLUCION EXITOSA - PRESTAFACIL")
    pdf.drawString(50, 760, "--------------------------------------------------")

    pdf.drawString(50, 720, f"Prestador: {nombre_usuario}")
    pdf.drawString(50, 700, f"ID del Item Devuelto: {id_item}")
    pdf.drawString(50, 680, f"Fecha de Devolucion: {fecha_dev}")
    pdf.drawString(50, 660, "Estado del Tramite: Certificado / A tiempo")

    pdf.drawString(50, 620, "--------------------------------------------------")
    pdf.drawString(50, 600, "Gracias por devolver el articulo a tiempo en PrestaFacil")
    pdf.drawString(50, 580, "==================================================")

    pdf.save()

    return nombre_archivo


def GenerarFacturaVenta(nombre_usuario, id_item, nombre_item, precio_compra):

    nombre_archivo = f"{nombre_usuario}_{id_item}.pdf"

    impuesto_conchudez = precio_compra * 0.23
    total = precio_compra + impuesto_conchudez

    pdf = canvas.Canvas(nombre_archivo)

    pdf.drawString(50, 800, "==================================================")
    pdf.drawString(50, 780, "FACTURA DE VENTA POR INCUMPLIMIENTO - PRESTAFACIL")
    pdf.drawString(50, 760, "==================================================")

    pdf.drawString(50, 720, f"Cliente / Ex-prestador: {nombre_usuario}")
    pdf.drawString(50, 700, f"ID del Artículo: {id_item}")
    pdf.drawString(50, 680, f"Artículo Vendido: {nombre_item}")

    pdf.drawString(50, 640, "MOTIVO DE LA VENTA:")
    pdf.drawString(50, 620, "El usuario excedió el tiempo límite de préstamo de 30 días.")
    pdf.drawString(50, 600, "Según las políticas de PrestaFacil, el artículo pasa")
    pdf.drawString(50, 580, "a ser propiedad obligatoria del prestador.")

    pdf.drawString(50, 540, "DETALLE DE COBRO:")
    pdf.drawString(50, 520, f"Subtotal (Precio Compra): ${precio_compra:.2f}")
    pdf.drawString(50, 500, f"Impuesto por Conchudez (23%): ${impuesto_conchudez:.2f}")

    pdf.drawString(50, 460, f"TOTAL A PAGAR: ${total:.2f}")

    pdf.drawString(50, 420, "==================================================")

    pdf.save()

    return total