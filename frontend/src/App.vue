<template>
  <div id="app">

    <nav>
      <div class="nav-wrapper blue darken-1">
        <a href="#" class="brand-logo center">Shipments Front</a>
      </div>
    </nav>

    <div class="container">

      <form>

          <label>TRACKING</label>
          <input type="text" placeholder="Tracking">
          <label>DESTINATION</label>
          <input type="text" placeholder="DESTINATION">
          <label>STATUS CODE</label>
          <input type="number" placeholder="STATUS CODE">

          <button class="waves-effect waves-light btn-small">Save<i class="material-icons left">save</i></button>

      </form>

      <table>

        <thead>

          <tr>

            <th>TRACKING</th>
            <th>DESTINATION</th>
            <th>STATUS CODE</th>
             <th>ACTIONS</th>
          </tr>

        </thead>

        <tbody>

          <tr>

            <td>kn-412304708-br</td>
            <td>CHINA</td>
            <td>99</td>
            <td>
              <button class="waves-effect btn-small blue darken-1"><i class="material-icons">create</i></button>
              <button class="waves-effect btn-small red darken-1"><i class="material-icons">delete_sweep</i></button>
            </td>

          </tr>

        </tbody>

      </table>

    </div>

  </div>
</template>

<script>
import Shipment from './services/shipments'

export default{
    mounted(){
        Shipment.listar().then(response => {
           console.log(response)
        })
    }
}
</script>

<style>

</style>
