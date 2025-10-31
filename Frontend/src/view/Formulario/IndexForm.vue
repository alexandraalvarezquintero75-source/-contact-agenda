<template>

  <!-- <DataTable /> -->

 <div class="d-flex justify-content-end gap-2 p-3">
    <AccionButtons @save="goForm" />
  </div>

</template>
<script setup>
// import DataTable from '@/components/design/molecules/DataTable.vue';
import AccionButtons from '@/components/design/molecules/AccionButtons.vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const goForm = () => {
  router.push({ name: 'form-forms' });
};
</script>

