<template>
  <div class="d-flex justify-content-end">
    <BaseButton
      class="btn-circle text-success hover-success"
      icon="bi bi-save"
      @click="$emit('save', entityId)"
    >
    </BaseButton>

    <BaseButton
      class="btn-circle text-danger"
      icon="bi bi-trash text-danger"
      @click="$emit('delete', entityId)"
    >
    </BaseButton>

    <BaseButton
      class="btn-circle text-success"
      icon="bi bi-eye text-success"
      @click="$emit('view', entityId)"
    >
    </BaseButton>

    <BaseButton
      class="btn-circle text-success"
      icon="bi bi-arrow-repeat text-success"
      @click="$emit('refresh')"
    >
    </BaseButton>

    <BaseButton
      class="btn-circle btn-warning text-warning"
      icon="bi bi-pencil"
      @click="$emit('edit', entityId)"
    >
    </BaseButton>
    <BaseButton
      class="btn-circle btn-warning text-warning"
      @click="$emit('save')"
      title="Guardar"
    >
      Guardar
    </BaseButton>
    <BaseButton
      type="button"
      class="btn btn-secondary rounded-pill px-4 py-2"
      @click="$emit('cancel')"
      title="Cancelar"
    >
      Cancelar
    </BaseButton>
  </div>
</template>

<script setup>
import BaseButton from "../atoms/BaseButton.vue";

defineProps({
  entityId: {
    type: [Number, String],
    required: false,
  },
});

</script>
