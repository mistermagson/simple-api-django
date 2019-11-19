import { http } from './config'

export default	{

	salvar:(shipment)=>{
		return http.post('shipment',shipment);
  },

	atualizar:(shipment)=>{
		return http.put('shipment',shipment);
  },

  listar:()=>{
		return http.get('shipments/')
  },

	deletar:(shipment)=>{
		return http.delete('shipment', { data: shipment })
	}
}