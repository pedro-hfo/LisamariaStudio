/** PT: Formata cêntimos em euros; evita valores monetários decimais no domínio.
 * EN: Format euro cents; avoid decimal monetary amounts in the domain.
 */
export function formatMoney(cents: number): string {
  if (!Number.isSafeInteger(cents)) throw new Error('Expected integer cents / Esperados cêntimos inteiros.');
  return new Intl.NumberFormat('pt-PT', { style: 'currency', currency: 'EUR' }).format(cents / 100);
}
