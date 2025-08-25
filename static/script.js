async function generarReporte() {
  const inicio = document.getElementById('fechaInicio').value;
  const fin = document.getElementById('fechaFin').value;
  const boton = document.querySelector('button');
  const loader = document.getElementById('loader');
  const inputInicio = document.getElementById('fechaInicio');
  const inputFin = document.getElementById('fechaFin');

  if (!inicio || !fin) {
    alert('Por favor selecciona ambas fechas');
    return;
  }
  if (new Date(inicio) > new Date(fin)) {
    alert('La fecha de inicio no puede ser posterior a la fecha de fin.');
    return;
  }

  // UI: bloquear y mostrar estado
  boton.disabled = true;
  inputInicio.disabled = true;
  inputFin.disabled = true;
  loader.textContent = 'Conectando, por favor espere...';
  loader.style.display = 'block';

  // Timeout opcional (p.ej., 120s)
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), 120000);

  try {
    const resp = await fetch('/procesar-reporte', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ fechaInicio: inicio, fechaFin: fin }),
      signal: controller.signal
    });

    // Ya respondió el servidor (pudo “despertar” la DB)
    loader.textContent = 'Generando reporte...';

    if (!resp.ok) {
      // intenta leer JSON de error; si no es JSON, muestra texto
      let msg = 'Error desconocido';
      try { const e = await resp.json(); msg = e.error || msg; }
      catch { msg = await resp.text() || msg; }
      throw new Error(msg);
    }

    const blob = await resp.blob();

    // Descargar
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'PEDELTA_PRORRATEO_CLOCKIFY.xlsx';
    document.body.appendChild(a);
    a.click();
    a.remove();
    URL.revokeObjectURL(url);

  } catch (err) {
    if (err.name === 'AbortError') {
      alert('La conexión tardó demasiado. Intenta nuevamente en unos segundos.');
    } else {
      console.error(err);
      alert(err.message || 'Error al generar el reporte');
    }
  } finally {
    clearTimeout(timeoutId);
    loader.style.display = 'none';
    boton.disabled = false;
    inputInicio.disabled = false;
    inputFin.disabled = false;
  }
}
