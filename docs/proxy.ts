import { createHash, timingSafeEqual } from 'node:crypto';
import { next } from '@vercel/functions';

const noStore = { 'Cache-Control': 'private, no-store' };

export default function proxy(request: Request) {
  const expected = process.env.DIRECTOR_AUTH_SHA256;
  if (!expected || !/^[0-9a-f]{64}$/.test(expected)) {
    return new Response('Director login is unavailable.', { status: 503, headers: noStore });
  }

  const credentials = request.headers.get('authorization')?.match(/^Basic ([A-Za-z0-9+/]+={0,2})$/i)?.[1];
  if (credentials) {
    const actual = createHash('sha256').update(credentials).digest();
    if (timingSafeEqual(actual, Buffer.from(expected, 'hex'))) {
      return next();
    }
  }

  return new Response('Sign in to view the Director Brief.', {
    status: 401,
    headers: { ...noStore, 'WWW-Authenticate': 'Basic realm="LP-AHJ Director Brief", charset="UTF-8"' },
  });
}
